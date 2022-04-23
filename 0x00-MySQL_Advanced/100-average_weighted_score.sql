-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
delimiter //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser( user_id INT )
BEGIN DECLARE overall_score FLOAT;

SET overall_score = (
SELECT SUM(score * weight) / SUM(weight) FROM users AS user
JOIN corrections ON user.id=corrections.user_id
JOIN projects ON corrections.project_id=projects.id
WHERE user.id=user_id);
UPDATE users

SET average_score = overall_score
WHERE id=user_id;
END //
delimiter ;
