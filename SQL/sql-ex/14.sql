Select
   s.class,
   s.name,
   c.country 
from
   ships s,
   classes c 
where
   s.class = c.class 
   and numguns >= 10