SELECT
   t1.STUDENT_ID,
   t1.TEST_ID,
   t1.GRADE_ID,
   t1.PERIOD_ID,
   t1.TEST_DATE,
   CASE
      WHEN
         p.passed = 1 
      THEN
         '+' 
      ELSE
         '-' 
   END
   as METREQ, 
   CASE
      WHEN
         p.last_date = STR_TO_DATE(t1.TEST_DATE, '%d-%b-%y') 
         and p.passed = 0 
      THEN
         1 
      ELSE
         0 
   END
   as IN_PROGRESS 
FROM
   `db`.`table1` t1 
   JOIN
      (
         SELECT
            PERIOD_ID,
            MAX(PASS_FAIL) as passed,
            MAX(STR_TO_DATE(TEST_DATE, '%d-%b-%y')) as last_date 
         FROM
            `db`.`table1` t1 
         GROUP BY
            PERIOD_ID
      )
      p 
      ON t1.PERIOD_ID = p.PERIOD_ID