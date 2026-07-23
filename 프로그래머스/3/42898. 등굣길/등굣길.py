from collections import deque

def solution(m, n, puddles):
    q = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)] # 최단거리
    count = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    count[0][0] = 1
    
    dxs = [1, 0]
    dys = [0, 1]
    
    road = [[1] * m for _ in range(n)]
    
    for y, x in puddles:
        road[x-1][y-1] = 0
    
    def in_range(x, y):
        return 0<=x<n and 0<=y<m
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and road[nx][ny]:
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    count[nx][ny] = count[x][y]
                elif visited[nx][ny] == visited[x][y] + 1:
                    count[nx][ny] += count[x][y]
    
    return count[n-1][m-1] % 1000000007