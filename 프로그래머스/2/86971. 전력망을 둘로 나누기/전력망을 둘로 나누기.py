from collections import deque

def solution(n, wires):
    # wires를 인접행렬로 바꾸기
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for i, j in wires:
        graph[i][j] = 1
        graph[j][i] = 1
    
    # 네트워크 개수 세기
    def bfs(x):
        visited = [False] * (n+1)
        q = deque([x])
        visited[x] = True
        cnt = 1
        
        while q:
            x = q.popleft()
            
            for i in range(1, n+1):
                if x != i and not visited[i] and graph[x][i]:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
        return cnt
    
    # 하나씩 돌면서 간선 끊어보기
    answer = float('inf')
    for a, b in wires:
        graph[a][b] = 0
        graph[b][a] = 0
        
        group1 = bfs(a)
        group2 = bfs(b)
        answer = min(answer, abs(group1 - group2))
        
        graph[a][b] = 1
        graph[b][a] = 1
    
    return answer
    
    