Select distinct
   product.maker 
From
   product 
   inner join
      pc 
      on product.model = pc.model 
where
   speed >= 450