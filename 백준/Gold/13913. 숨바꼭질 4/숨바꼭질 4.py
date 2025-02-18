from collections import deque

def print_path(prev, target):
    path = []
    while target != -1:
        path.append(target)
        target = prev[target]
    print(*path[::-1])


def bfs(start, target):
    if start == target:
        print(0)
        print(start)
        return 
    
    visited = [-1] * 100001
    prev = [-1] * 100001
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur_pos = q.popleft()

        for next_pos in (cur_pos - 1, cur_pos +1, cur_pos * 2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                prev[next_pos] = cur_pos
                visited[next_pos] = visited[cur_pos] + 1
                q.append(next_pos)
            
            if next_pos == target:
                print(visited[next_pos])
                print_path(prev, target)
                return

n, k = map(int, input().split())
bfs(n, k)