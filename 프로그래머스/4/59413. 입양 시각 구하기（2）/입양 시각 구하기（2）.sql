WITH RECURSIVE HOUR_TABLE AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1
    FROM HOUR_TABLE
    WHERE HOUR < 23
)

SELECT H.HOUR, IFNULL(COUNT(A.DATETIME), 0) AS COUNT
FROM HOUR_TABLE H
LEFT JOIN ANIMAL_OUTS A
    ON H.HOUR = HOUR(A.DATETIME)
GROUP BY H.HOUR
ORDER BY H.HOUR ASC;