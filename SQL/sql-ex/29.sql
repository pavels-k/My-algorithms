Select
   Income_o.point,
   Income_o.[date],
   Income_o.inc,
   Outcome_o .out 
from
   Income_o 
   left join
      Outcome_o 
      on Income_o.point = Outcome_o.point 
      and Income_o.[date] = Outcome_o.[date] 
   union
   Select
      Outcome_o.point,
      Outcome_o.[date],
      Income_o.inc,
      Outcome_o .out 
   from
      Income_o 
      right join
         Outcome_o 
         on Income_o.point = Outcome_o.point 
         and Income_o.[date] = Outcome_o.[date]