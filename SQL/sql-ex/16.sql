Select distinct
   a.model,
   b.model,
   a.speed,
   b.ram 
from
   pc a,
   pc b 
where
   a.speed = b.speed 
   and a.ram = b.ram 
   and a.model > b.model