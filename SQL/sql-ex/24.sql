select distinct
   product.model 
from
   product,
   (
      select
         max(ma.m) as val 
      from
         (
            select
               max(pc.price) as m 
            from
               pc 
            union
            select
               max(laptop.price) 
            from
               laptop 
            union
            select
               max(printer.price) 
            from
               printer
         )
         as ma 
   )
   as db,
   pc,
   laptop,
   printer 
where
   (
      pc.price = db.val 
      and product.model = pc.model
   )
   or 
   (
      laptop.price = db.val 
      and laptop.model = product.model
   )
   or 
   (
      printer.price = db.val 
      and printer.model = product.model
   )