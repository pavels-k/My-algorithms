select
   p.maker,
   count(p.model) 
from
   product p 
where
   p.type = 'PC' 
GROUP BY
   p.maker 
having
   count(p.model) > 2