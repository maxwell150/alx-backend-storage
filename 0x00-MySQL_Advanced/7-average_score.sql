-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

delimeter //
create procedure ComputeOverallScoreForUser(
	in user_id int
)
begin
   update users
   set overall_score = (select AVG(score)
    from corrections
	where corrections.user_id=user_id
	group BY corrections.user_id )
    where id=user_id;
end //
delimeter;
