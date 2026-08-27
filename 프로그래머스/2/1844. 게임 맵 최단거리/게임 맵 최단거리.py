from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * m for _ in range(n)]
    
    q = deque([(0, 0)])
    visited[0][0] = 1
    
    def in_range(r, c):
        return 0<= r < n and 0<= c < m
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            
            if in_range(nr, nc) and not visited[nr][nc] and maps[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    
    return -1 if visited[n-1][m-1] == 0 else visited[n-1][m-1]
            
    