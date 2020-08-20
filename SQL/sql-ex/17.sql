select distinct
   p.type,
   l.model,
   l.speed 
from
   laptop l 
   join
      product p 
      ON p.model = l.model 
where
   l.speed < (
   select
      min(speed) 
   from
      pc)