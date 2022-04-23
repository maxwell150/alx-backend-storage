-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
delimiter //
create procedure ComputeAverageScoreForUser( in user_id int )
begin
   update users
   set overall_score = (select AVG(score)
    from corrections
	where corrections.user_id=user_id
	group BY corrections.user_id )
    where id=user_id;
end //
delimiter;
