SELECT
    ingredient_type, 
    SUM(total_order) AS 'total_order'
FROM first_half
INNER JOIN icecream_info USING (flavor)
GROUP BY ingredient_type
ORDER BY total_order ASC;