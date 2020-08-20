Select
   i.point,
   i.[date],
   sum(o.outco),
   sum(i.inco) 
from
   (
      Select
         Income.point,
         Income.[date],
         sum(Income.inc) as inco 
      from
         Income 
      group by
         Income.point,
         Income.[date] 
   )
   as i 
   left join
      (
         Select
            Outcome.point,
            Outcome.[date],
            sum(Outcome.out) as outco 
         from
            Outcome 
         group by
            Outcome.point,
            Outcome.[date] 
      )
      as o 
      on i.point = o.point 
      and i.[date] = o.[date] 
group by
   i.point,
   i.[date] 
union
Select
   o.point,
   o.[date],
   sum(o.outco),
   sum(i.inco) 
from
   (
      Select
         Income.point,
         Income.[date],
         sum(Income.inc) as inco 
      from
         Income 
      group by
         Income.point,
         Income.[date] 
   )
   as i 
   right join
      (
         Select
            Outcome.point,
            Outcome.[date],
            sum(Outcome.out) as outco 
         from
            Outcome 
         group by
            Outcome.point,
            Outcome.[date] 
      )
      as o 
      on i.point = o.point 
      and i.[date] = o.[date] 
group by
   o.point,
   o.[date]