from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    visited = [[0] * m for _ in range(n)]
    
    def in_range(x, y):
        return 0<=x<n and 0<=y<m
    
    # bfs
    q.append((0, 0))
    visited[0][0] = 1
    
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and not visited[nx][ny] and maps[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1   
                q.append((nx, ny))
    
    return visited[n-1][m-1] if visited[n-1][m-1] else -1