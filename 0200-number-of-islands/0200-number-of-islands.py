from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def in_range(r, c):
            return 0<=r<m and 0<=c<n

        def bfs(r, c):
            q = deque([(r, c)])
            visited[r][c] = True

            drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

            while q:
                r, c = q.popleft()

                for dr, dc in zip(drs, dcs):
                    nr, nc = r + dr, c + dc

                    if in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        visited[nr][nc] = True


        answer = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    bfs(i, j)
                    answer += 1
        
        return answer