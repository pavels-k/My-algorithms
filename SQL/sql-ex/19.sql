Select
   p.maker,
   avg(l.screen) 
from
   product p,
   laptop l 
where
   p.model = l.model 
group by
   p.maker