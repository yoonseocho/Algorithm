from collections import deque

def solution(maps):
    q = deque()
    
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    cnt = 0
    
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    q.append((0, 0))
    visited[0][0] = 1
    
    def in_range(x, y):
        return 0<= x < n and 0<= y < m
    
    def bfs():
        nonlocal cnt
        
        # if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0:
        #     return -1
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and not visited[nx][ny] and maps[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    bfs()
    return visited[n-1][m-1] if visited[n-1][m-1] else -1