from collections import deque

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
        
        while q:
            r, c = q.popleft()

            for i in range(n):
                matrix[r][i] = 0
            
            for i in range(m):
                matrix[i][c] = 0
        