SELECT
    HOUR(datetime) AS '시간대', 
    COUNT(*) AS '건수'
FROM animal_outs
GROUP BY 시간대
HAVING 시간대 BETWEEN 9 AND 19
ORDER BY 시간대 ASC;