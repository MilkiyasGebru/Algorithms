# Write your MySQL query statement below

select Visits.customer_id as customer_id, count(Visits.customer_id) as "count_no_trans" from Visits left join Transactions on 
Transactions.visit_id = Visits.visit_id 
where Transactions.visit_id is null
group by Visits.customer_id