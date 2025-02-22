from collections import deque

def bfs(start, target):
    if start == target:
        print(0)
        print(1)
        return
    visited = [-1] * 100001
    count = [0] * 100001
    q = deque()
    q.append(start)
    visited[start] = 0
    count[start] = 1
    min_level = float("inf")
    
    while q:
        cur_pos = q.popleft()

        if visited[cur_pos] > min_level:
            break

        for next_pos in (cur_pos - 1, cur_pos + 1, cur_pos * 2):
            if 0 <= next_pos <= 100000:
                if visited[next_pos] == -1:
                    q.append(next_pos)
                    visited[next_pos] = visited[cur_pos] + 1
                    count[next_pos] = count[cur_pos]
            
                elif visited[next_pos] == visited[cur_pos] + 1:
                    count[next_pos] += count[cur_pos]

                if next_pos == target:
                    min_level = visited[next_pos]
    
    print(min_level)
    print(count[target])
    return

n, k = map(int, input().split())
bfs(n, k)