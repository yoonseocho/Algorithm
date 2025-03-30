from collections import deque

def bfs(maps):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    row = len(maps)
    col = len(maps[0])
    
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
    
        for dx, dy in delta:
            next_x = x + dx
            next_y = y + dy
            
            if 0 <= next_x < row and 0 <= next_y < col:
                if maps[next_x][next_y] == 1:
                    maps[next_x][next_y] = maps[x][y] + 1
                    q.append((next_x, next_y))
    
    return maps[row - 1][col - 1] if maps[row - 1][col - 1] > 1 else -1

def solution(maps):
    return bfs(maps)