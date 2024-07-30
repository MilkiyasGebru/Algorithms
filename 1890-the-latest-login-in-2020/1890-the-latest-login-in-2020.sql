# Write your MySQL query statement below
select user_id, max(last_stamp) as 'last_stamp' from (select user_id, time_stamp as 'last_stamp'  from Logins
where time_stamp >= '2020-01-01 00:00:01' and time_stamp <= '2020-12-31 23:59:59' order by time_stamp DESC) as db group by user_id 