SELECT DISTINCT
   maker 
FROM
   Product 
where
   type = 'printer' 
   and maker in 
   (
      select
         maker 
      from
         product 
      where
         model in 
         (
            select
               model 
            from
               pc 
            where
               speed = 
               (
                  select
                     max(speed) 
                  from
                     (
                        select
                           pc.speed 
                        from
                           pc 
                        where
                           pc.ram = 
                           (
                              select
                                 min(pc.ram) 
                              from
                                 pc
                           )
                     )
                     as pv
               )
               and pc.ram = 
               (
                  select
                     min(pc.ram) 
                  from
                     pc
               )
         )
   )