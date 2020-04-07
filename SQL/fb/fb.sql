-- The names of all salespeople that have an order with Samsonic
select name from salesperson s join orders o on
s.id = o.salesperson_id join customer c on o.cust_id = c.id
where c.name = "Samsonic";

-- the names of all salespeople that do not have any order with samsonic
select name from salesperson s join orders o on
s.id = o.salesperson_id join customer c on o.cust_id = c.id
where c.name != "Samsonic";

-- the names of salespeople that have 2 or more orders
select s.name, count(distinct o.number) as orders
from salesperson s join orders o on s.id = o.salesperson_id
group by s.name having orders >= 2;

-- the names and ages of all salespersons must having a salary of 100,000 or greater
select name, age from salesperson where salary >= 100000;

-- what sales people have sold more than 1400 total units
select s.name, sum(o.amount) as units
from salesperson s join orders o on s.id = o.salesperson_id
group by s.name having units > 1400;

-- when was the earliest and latest order made to Samony
select max(o.order_date), min(o.order_date)
from orders o join customer c on o.cust_id = c.id
where c.name = 'Samony';
