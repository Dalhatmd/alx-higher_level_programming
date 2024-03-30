-- displays the average temperature of an imported table dump (temperature)

SELECT city, AVG(value) AS avg_temp FROM temperature GROUP BY city ORDER BY avg_temp DESC;
