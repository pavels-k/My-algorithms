select
   avg(s.price) 
from
   (
      select
         pc.price 
      from
         pc 
      where
         pc.model in 
         (
            select
               product.model 
            from
               product 
            where
               maker = 'A'
         )
      union all
      select
         laptop.price 
      from
         laptop 
      where
         laptop.model in 
         (
            select
               product.model 
            from
               product 
            where
               maker = 'A'
         )
   )
   as s