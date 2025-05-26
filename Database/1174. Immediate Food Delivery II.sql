# Write your MySQL query statement below
with ranked_orders as (
    select delivery_id , customer_id, order_date, customer_pref_delivery_date, 
    dense_rank() over (partition by customer_id order by order_date) as rk
    from Delivery
),
total_first_orders as (
    select count(delivery_id) as total_order_count from
    ranked_orders
    where rk = 1
),
total_immediate_first_orders as (
    select count(delivery_id) as immediate_order_count from
    ranked_orders
    where rk = 1 and order_date = customer_pref_delivery_date
)
select round((immediate_order_count/total_order_count)*100,2) as immediate_percentage 
from total_first_orders,total_immediate_first_orders
