with abc as (select 
product_id, new_price from (select *, rank() over (partition by product_id order by change_date desc) as rk
from Products
where change_date <= "2019-08-16") as xyz
where rk = 1)
select distinct p.product_id, ifnull(abc.new_price,10) as price
from Products p
left join
abc
on p.product_id = abc.product_id
