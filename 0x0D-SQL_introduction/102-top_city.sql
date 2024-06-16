-- The script displays the top 3 cities temperature during July and August
-- Odered by temperature (descending)

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
