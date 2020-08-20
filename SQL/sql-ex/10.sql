Select
   model,
   price 
from
   printer 
where
   price in 
   (
      select
         MAX(price) 
      from
         printer
   )