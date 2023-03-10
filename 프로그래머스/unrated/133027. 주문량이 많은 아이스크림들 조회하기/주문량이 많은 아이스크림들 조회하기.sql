SELECT FLAVOR
FROM (
    SELECT
        FLAVOR, 
        SUM(TOTAL_ORDER) AS TOTAL
    FROM FIRST_HALF
    GROUP BY FLAVOR) AS F
INNER JOIN (
    SELECT
        FLAVOR, 
        SUM(TOTAL_ORDER) AS TOTAL
    FROM JULY
    GROUP BY FLAVOR
) AS J USING (FLAVOR)
ORDER BY (F.TOTAL + J.TOTAL) DESC
LIMIT 3;