--  script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
create trigger decrement
after insert on orders for each row
update items set quantity = quantity - new.number where name = new.item_name;
