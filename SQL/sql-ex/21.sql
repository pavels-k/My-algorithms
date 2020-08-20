Select
   maker,
   max(price) 
from
   product,
   pc 
where
   product.model = pc.model 
group by
   maker