Select
   product.maker,
   AVG(PC.hd) 
from
   product 
   inner join
      pc 
      on pc.model = product.model 
where
   product.maker in 
   (
      select distinct
         maker 
      from
         product 
      where
         type = 'printer'
   )
group by
   product.maker