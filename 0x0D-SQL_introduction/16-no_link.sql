-- Displays all records except records without a name value
-- Order by scores in descending order

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
