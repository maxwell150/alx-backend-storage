-- script that creates a stored procedure AddBonus that adds a new correction for a student.
delimiter //
create procedure AddBonus (
	in user_id integer,
	in project_name varchar(255),
	in score integer
)
begin
    insert into projects (name)
    select project_name from dual
    where NOT EXISTS (select * from projects where name=project_name LIMIT 1);
    insert into corrections (user_id, project_id, score)
    values(user_id, (select id from projects where name=project_name), score);
end //
delimiter ;
