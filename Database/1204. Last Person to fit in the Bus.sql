select person_name from (
    select person_name, sum(weight) over (order by turn) as cum_weights
    from Queue
) as abc
where cum_weights <= 1000
order by cum_weights desc
limit 1
