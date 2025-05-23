select id, 'Root' as type from Tree where p_id is null
union 
select id, 'Inner' as type from Tree t where exists(select 1 from Tree where p_id = t.id) and p_id is not null
union
select id, 'Leaf' as type from Tree t where not exists(select 1 from Tree where p_id = t.id) and p_id is not null