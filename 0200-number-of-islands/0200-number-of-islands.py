from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
        visited = [[False] * n for _ in range(m)]

        def in_range(r, c):
            return 0<=r<m and 0<=c<n

        def bfs(r, c):
            q = deque([(r, c)])
            visited[r][c] = True

            while q:
                r, c = q.popleft()

                for dr, dc in zip(drs, dcs):
                    nr, nc = r+dr, c+dc
                    if in_range(nr, nc) and grid[nr][nc] == "1" and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1
        
        return cnt