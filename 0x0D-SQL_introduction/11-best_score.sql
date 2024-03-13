-- Selects the best scores from the table 

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
