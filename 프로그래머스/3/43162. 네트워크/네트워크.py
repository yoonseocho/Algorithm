from collections import deque

def solution(n, computers):
    visited = [False] * n
    
    def bfs(k):
        q = deque([k])
        visited[k] = True
        
        while q:
            cur = q.popleft()
            
            for i in range(n):
                if i != cur and not visited[i] and computers[cur][i]:
                    q.append(i)
                    visited[i] = True
    
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer