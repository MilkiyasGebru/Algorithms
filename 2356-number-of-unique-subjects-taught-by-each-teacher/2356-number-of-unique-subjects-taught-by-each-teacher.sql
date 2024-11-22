# Write your MySQL query statement below

select teacher_id, Count(distinct subject_id) as cnt from Teacher
Group by teacher_id