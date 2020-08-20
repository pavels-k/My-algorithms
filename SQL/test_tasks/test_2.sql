# MYSQL
SELECT
   data1.yearmonth AS Год_и_месяц_появления_пользователя_в_системе,
   data1.column_2 AS Количество_новых_пользователей_пришедших_в_этом_месяце,
   data1.column_3 AS Количество_пользователей_вернувшихся_на_второй_календарный_месяц_после_регистрации,
    ifnull(concat(round( 100*data1.column_3 / data1.column_2), '%'), 'Деление на 0') AS Вероятность_возврата
FROM
   (
      SELECT
         nested_table1.yearmonth,
         nested_table1.column_2 AS column_2,
         ifnull(nested_table2.column_3, 0) AS column_3 
      FROM
         (
            SELECT
               date_format(event_timestamp, '%Y-%m') AS yearmonth,
               COUNT(event_name) AS column_2 
            FROM
               mydb.test 
            WHERE
               event_name = 'registration' 
            GROUP BY
               date_format(event_timestamp, '%Y-%m')
         )
         AS nested_table1 
         LEFT JOIN
            (
               SELECT
(date_format(event_timestamp, '%Y-%m')) AS yearmonth,
                  COUNT(DISTINCT user_id) AS column_3 
               FROM
                  mydb.test 
               WHERE
                  (
                     MONTH(event_timestamp) + 12 * YEAR(event_timestamp)
                  )
                  IN 
                  (
                     SELECT
                        MONTH(event_timestamp) + 12 * YEAR(event_timestamp) + 1 
                     FROM
                        mydb.test 
                     WHERE
                        event_name = 'registration'
                  )
                  AND event_name != 'registration' 
               GROUP BY
                  yearmonth
            )
            AS nested_table2 
            ON nested_table1.yearmonth = nested_table2.yearmonth 
         UNION
         SELECT
            nested_table2.yearmonth,
            ifnull(nested_table1.column_2, 0) AS column_2,
            nested_table2.column_3 AS column_3 
         FROM
            (
               SELECT
                  date_format(event_timestamp, '%Y-%m') AS yearmonth,
                  COUNT(event_name) AS column_2 
               FROM
                  mydb.test 
               WHERE
                  event_name = 'registration' 
               GROUP BY
                  date_format(event_timestamp, '%Y-%m')
            )
            AS nested_table1 
            RIGHT JOIN
               (
                  SELECT
(date_format(event_timestamp, '%Y-%m')) AS yearmonth,
                     COUNT(distinct user_id) AS column_3 
                  FROM
                     mydb.test 
                  WHERE
                     (
                        MONTH(event_timestamp) + 12 * YEAR(event_timestamp)
                     )
                     IN
                     (
                        SELECT
                           MONTH(event_timestamp) + 12 * YEAR(event_timestamp) + 1 
                        FROM
                           mydb.test 
                        WHERE
                           event_name = 'registration'
                     )
                     AND event_name != 'registration' 
                  GROUP BY
                     yearmonth
               )
               AS nested_table2 
               ON nested_table1.yearmonth = nested_table2.yearmonth 
         ORDER BY
            yearmonth 
   )
   AS data1 ;