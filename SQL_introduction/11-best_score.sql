-- Listing all records with a score >= 10 of the second_table

SELECT score, name from second_table
WHERE score >= 10 ORDER BY score DESC;