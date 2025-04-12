from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    
    for next_v in graph[start]:
        if not visited[next_v]:
            dfs(next_v)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur_v = q.popleft()
        print(cur_v, end = " ")

        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)
    

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

# dfs
visited = [False] * (n + 1)
dfs(v)
print()
# bfs
visited = [False] * (n + 1)
bfs(v)
