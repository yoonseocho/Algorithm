# SELECT
#     SUM(G.SCORE) AS SCORE,
#     E.EMP_NO AS EMP_NO,
#     E.EMP_NAME AS EMP_NAME,
#     E.POSITION AS POSITION,
#     E.EMAIL AS EMAIL
# FROM HR_EMPLOYEES E
# JOIN HR_GRADE G
#     ON E.EMP_NO = G.EMP_NO
# GROUP BY EMP_NO
# HAVING SUM(G.SCORE) IN (
#                         SELECT 
#                             MAX(SCORE)
#                         FROM (
#                             SELECT
#                                SUM(SCORE) AS SCORE
#                             FROM HR_GRADE
#                             GROUP BY EMP_NO
#                         ) T
#                     )

WITH TMP AS (
    SELECT
        EMP_NO,
        SUM(SCORE) AS SCORE,
        RANK() OVER (ORDER BY SUM(SCORE) DESC) AS RNK
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT
    T.SCORE AS SCORE,
    E.EMP_NO AS EMP_NO,
    E.EMP_NAME AS EMP_NAME,
    E.POSITION AS POSITION,
    E.EMAIL AS EMAIL
FROM TMP T
JOIN HR_EMPLOYEES E
    ON T.EMP_NO = E.EMP_NO
WHERE T.RNK = 1



