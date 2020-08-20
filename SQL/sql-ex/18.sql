select distinct
   product.maker,
   price 
from
   product,
   printer 
where
   color = 'y' 
   and product.model = printer.model 
   and price = 
   (
      SELECT
         min(price) 
      FROM
         printer 
      where
         color = 'y'
   )