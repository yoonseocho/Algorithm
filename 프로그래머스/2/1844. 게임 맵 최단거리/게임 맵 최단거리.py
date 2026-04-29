from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    dist = [[0] * m for _ in range(n)]
    q = deque()
    
    def in_range(x, y):
        return 0<=x<n and 0<=y<m
    
    def bfs(x, y):
        # if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0:
        #     return -1
        
        q.append((x, y))
        dist[x][y] = 1
        
        while q:
            x, y = q.popleft()
            
            if x == n-1 and y == m-1:
                return dist[n-1][m-1]
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and maps[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        return -1
    
    return bfs(0, 0)
    
                
        