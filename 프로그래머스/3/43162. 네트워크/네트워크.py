from collections import deque

def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    def bfs(x):
        q = deque([x])
        visited[x] = True
        
        while q:
            x = q.popleft()
            
            for i in range(n):
                if x != i and not visited[i] and computers[x][i]:
                    q.append(i)
                    visited[i] = True
        
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
    
    return cnt