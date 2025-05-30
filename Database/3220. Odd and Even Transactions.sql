select 
transaction_date,
sum(case when mod(amount,2) != 0 then amount else 0 end) as odd_sum,
sum(case when mod(amount,2) = 0 then amount else 0 end) as even_sum
from transactions
group by transaction_date
order by transaction_date
