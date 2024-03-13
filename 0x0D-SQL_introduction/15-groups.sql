-- Returns the scores and number of times the score appears

SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
