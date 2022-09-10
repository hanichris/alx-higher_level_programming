-- Show the average temperature by city sorted in descending order by the temperature.
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
