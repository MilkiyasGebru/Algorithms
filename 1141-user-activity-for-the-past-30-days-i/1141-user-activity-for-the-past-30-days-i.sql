# Write your MySQL query statement below

select activity_date as day, count(distinct user_id) as active_users from Activity Group by day Having active_users > 0 AND activity_date >= '2019-06-28' AND activity_date <= '2019-07-27'