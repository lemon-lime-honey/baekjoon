SELECT PLACES.ID, PLACES.NAME, HOST_ID
FROM PLACES
INNER JOIN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(ID) >= 2
) NEWTABLE USING(HOST_ID)
ORDER BY ID ASC;