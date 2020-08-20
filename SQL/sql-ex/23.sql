Select distinct
   maker 
from
   product 
   join
      pc 
      on product.model = pc.model 
where
   speed >= 750 
   and maker in 
   (
      select
         maker 
      from
         product 
         join
            laptop 
            on product.model = laptop.model 
      where
         speed >= 750
   )