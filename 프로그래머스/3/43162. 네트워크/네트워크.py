from collections import deque

def solution(n, computers):
    visited = [False]*n
    q = deque()
    
    def bfs(x):
        visited[x] = True
        q.append(x)
        
        while q:
            x = q.popleft()
            
            # 인접행렬 순회
            for k in range(n):
                if x != k and computers[x][k] and not visited[k]:
                    visited[k] = True
                    q.append(k)
    
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
    
    return cnt