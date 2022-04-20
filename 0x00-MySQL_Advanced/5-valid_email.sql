-- script that creates a trigger that resets the attribute valid_email only when the email has been changed.
delimiter //
create trigger reset_valid
before update on users
for each row
begin
    if new.email != old.email
    then set new.valid_email = 0;
end if;
end; //
