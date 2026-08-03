-- 코드를 작성해주세요
SELECT 
    SUM(G.SCORE) AS SCORE,
    E.EMP_NO AS EMP_NO,
    E.EMP_NAME AS EMP_NAME,
    E.POSITION AS POSITION,
    E.EMAIL AS EMAIL
FROM HR_DEPARTMENT D
JOIN HR_EMPLOYEES E
    ON D.DEPT_ID = E.DEPT_ID
JOIN HR_GRADE G
    ON E.EMP_NO = G.EMP_NO
GROUP BY G.EMP_NO
HAVING SUM(G.SCORE) = (
                        SELECT MAX(TOTAL)
                        FROM (SELECT SUM(SCORE) AS TOTAL
                            FROM HR_GRADE
                            GROUP BY EMP_NO) T
                        )