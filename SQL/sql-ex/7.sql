SELECT
   model,
   price 
FROM
   PC 
WHERE
   model IN 
   (
      SELECT
         model 
      FROM
         Product 
      WHERE
         maker = 'B' 
         AND type = 'PC' 
   )
UNION
SELECT
   model,
   price 
FROM
   Laptop 
WHERE
   model IN 
   (
      SELECT
         model 
      FROM
         Product 
      WHERE
         maker = 'B' 
         AND type = 'Laptop' 
   )
UNION
SELECT
   model,
   price 
FROM
   Printer 
WHERE
   model IN 
   (
      SELECT
         model 
      FROM
         Product 
      WHERE
         maker = 'B' 
         AND type = 'Printer' 
   )