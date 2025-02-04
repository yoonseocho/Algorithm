from collections import deque

def bfs(start, target):
    visited = [-1] * 100001
    prev = [-1] * 100001
    if start == target:
        print(0)
        print(start)
        return 
    q = deque()
    q.append(start)
    visited[start] = 0
    min_steps = float('inf')

    while q:
        cur_pos = q.popleft()

        if visited[cur_pos] > min_steps:
            break

        for next_pos in (cur_pos - 1, cur_pos +1, cur_pos * 2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                prev[next_pos] = cur_pos
                visited[next_pos] = visited[cur_pos] + 1
                q.append(next_pos)
            
            if next_pos == target:
                min_steps = visited[next_pos]
    
    print(min_steps)
    output = [target]
    temp = prev[target]
    while temp != -1:
        output.append(temp)
        temp = prev[temp]
    print(*output[::-1])
    return 
            
n, k = map(int, input().split())
bfs(n, k)