# Write your MySQL query statement below
with abc as (
    select user_id, count(distinct movie_id) as num 
    from MovieRating 
    group by user_id
), def as (
    select movie_id, sum(rating)/count(distinct user_id) as avg_rating from MovieRating
    where created_at between "2020-02-01" and "2020-02-29"
    group by movie_id
),
top_user as ( select name as results from (
    select user_id, dense_rank() over (order by num desc) as rk from abc
) as xyz
join Users u on u.user_id = xyz.user_id
where rk = 1
order by name limit 1
),
top_movie as ( select title as results from (
    select movie_id, dense_rank() over (order by avg_rating desc) as rk from def
) as ghi
join Movies m on ghi.movie_id = m.movie_id
where rk = 1
order by title limit 1
)
select * from top_user 
union all
select * from top_movie
