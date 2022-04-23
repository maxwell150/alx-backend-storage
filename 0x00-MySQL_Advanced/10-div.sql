-- SQL script that creates a function SafeDiv that divides (and returns) the
-- first by the second number or returns 0 if the second number is equal to 0.
delimiter //
drop function if exists `SafeDiv`;
create function SafeDiv(a INT, b INT)
returns float deterministic
begin
    if (b = 0)
    then
        RETURN (0);
    else
        RETURN (a / b);
    end if;
end //
delimiter ;
