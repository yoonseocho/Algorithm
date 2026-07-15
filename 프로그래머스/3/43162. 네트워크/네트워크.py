from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def bfs(start):
        q = deque([start])
        visited[start] = True
        
        while q:
            current = q.popleft()
            
            for i in range(n):
                if i != current and not visited[i] and computers[current][i]:
                    q.append(i)
                    visited[i] = True
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer
        
    
    