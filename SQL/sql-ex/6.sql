Select distinct
   product.maker,
   laptop.speed 
From
   product 
   inner join
      laptop 
      on product.model = laptop.model 
where
   hd >= 10