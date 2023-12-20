# Write your MySQL query statement below
(select u.name as results
    from MovieRating as m left join Users as u on m.user_id = u.user_id 
    group by m.user_id 
    order by count(m.rating) desc, u.name asc
    limit 1
)
union all
(select m.title as results
 from MovieRating as mr left join Movies as m on mr.movie_id = m.movie_id
 where mr.created_at <= "2020-02-28" and mr.created_at >= "2020-02-01"
 group by mr.movie_id
 order by avg(mr.rating) desc, m.title asc
 limit 1
)