from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n)]
    visited = [-1] * n
    
    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # 인접행렬 bfs
    q = deque()
    
    q.append(0)
    visited[0] = 0
    
    while q:
        x = q.popleft()
        
        for k in graph[x]:
            if visited[k] == -1:
                visited[k] = visited[x] + 1
                q.append(k)
    
    return visited.count(max(visited))