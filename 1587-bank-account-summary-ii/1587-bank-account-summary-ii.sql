# Write your MySQL query statement below

select name , balance  from (select Users.name,sum(Transactions.amount) as "balance" from Users join
Transactions on Users.account = Transactions.account
group by name ) as sub where balance > 10000 

