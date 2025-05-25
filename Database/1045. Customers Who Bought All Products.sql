select customer_id from (
select distinct customer_id as customer_id, 
group_concat(distinct product_key order by product_key separator ',') as abc
from Customer
group by customer_id) as xyz
where xyz.abc = (select group_concat(distinct product_key order by product_key separator ',') from Product)
