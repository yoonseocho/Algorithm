from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0<=r<n and 0<=c<m
    
    def bfs(r, c):
        q = deque([(r, c)])
        visited[r][c] = 1
        
        while q:
            cur_r, cur_c = q.popleft()
            
            for dr, dc in zip(drs, dcs):
                nr, nc = cur_r + dr, cur_c + dc
                
                if in_range(nr, nc) and not visited[nr][nc] and maps[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
    
    bfs(0, 0)
    
    return visited[n-1][m-1] if visited[n-1][m-1] else -1