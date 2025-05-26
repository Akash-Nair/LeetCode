select s.user_id, ifnull(round(confirmation_rate,2),0) as confirmation_rate from Signups s
left join (
    select user_id, sum(action='confirmed')/count(*) as confirmation_rate
    from Confirmations 
    group by user_id
) as abc
on s.user_id = abc.user_id
