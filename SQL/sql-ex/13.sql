select
   avg(speed) 
from
   product 
   inner join
      pc 
      on pc.model = product.model 
      and product.maker = 'A'