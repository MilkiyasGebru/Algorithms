# Write your MySQL query statement below
select EmployeeUNI.unique_id as 'unique_id', Employees.name as 'name' From Employees left join EmployeeUNI on EmployeeUNI.id = Employees.id