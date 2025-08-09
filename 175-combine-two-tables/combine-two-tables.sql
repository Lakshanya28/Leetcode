# Write your MySQL query statement below
select firstname,lastname,city, state 
from address a
right join person p 
    on p.personId=a.personId