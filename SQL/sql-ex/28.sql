select
   count(maker) 
from
   product 
where
   maker in 
   (
      select
         maker 
      from
         product 
      group by
         maker 
      having
         count(model) < 2
   )