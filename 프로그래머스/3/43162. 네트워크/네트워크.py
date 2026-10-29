from collections import deque, defaultdict

def solution(n, computers):
    graph = defaultdict(set)
    visited = [False] * n
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                graph[i].add(j)
                graph[j].add(i)
    
    print(graph)
    
    def bfs(num):
        q = deque([num])
        visited[num] = True
        
        while q:
            cur_num = q.popleft()
            
            for c in graph[cur_num]:
                if c != cur_num and not visited[c]:
                    visited[c] = True
                    q.append(c)
            
    
    network_cnt = 0
    for k in range(n):
        if not visited[k]:
            bfs(k)
            network_cnt += 1
    
    return network_cnt
    