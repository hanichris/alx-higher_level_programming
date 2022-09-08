-- List all the records >= 10.
-- The list should be ordered in descending order of the score.
-- The list should also be displayed first by the score then the name columns
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
