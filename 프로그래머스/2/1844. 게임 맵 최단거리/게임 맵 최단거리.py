from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    dist = [[0]*m for _ in range(n)]
    q = deque()
    
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    def in_range(x, y):
        return 0<=x<n and 0<=y<m
    
    def bfs(x, y):
        q.append((x, y))
        dist[x][y] = 1
        
        while q:
            x, y = q.popleft()
            
            if x == n-1 and y == m-1:
                return dist[x][y]
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                
                if in_range(nx, ny) and not dist[nx][ny] and maps[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        
        return -1
                
                
    return bfs(0, 0)