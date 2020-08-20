Select
   speed,
   avg(price) as avg 
from
   pc 
group by
   speed 
having
   speed > 600