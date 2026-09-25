from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        q = deque()

        drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

        def in_range(r, c):
            return 0<=r<m and 0<=c<n

        
         # 모든 썩은 오렌지를 한꺼번에 큐에 넣고 시작
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while q:
            cur_r, cur_c = q.popleft()

            for dr, dc in zip(drs, dcs):
                nr, nc = cur_r + dr, cur_c + dc

                if in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
                    q.append((nr, nc))
        
        flag = False
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    flag = True
                    break
            if flag:
                break

        return -1 if flag else max(map(max, visited))

