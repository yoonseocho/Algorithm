from collections import deque

def bfs(start, target):
    visited = [-1] * 100001
    if start == target:
        return 0
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        cur_pos = q.popleft()

        for next_pos in (cur_pos-1, cur_pos+1, cur_pos*2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                visited[next_pos] = visited[cur_pos] + 1
                q.append(next_pos)

                if next_pos == target:
                    return visited[next_pos]

N, K = map(int, input().split())
print(bfs(N, K))