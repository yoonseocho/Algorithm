from collections import deque

def bfs(start, target):
    if start == target:
        print(0)
        print(start)
        return
    visited = [-1] * 100001
    prev_path = [-1] * 100001
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur_pos = q.popleft()

        for next_pos in (cur_pos - 1, cur_pos + 1, cur_pos * 2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                q.append(next_pos)
                visited[next_pos] = visited[cur_pos] + 1
                prev_path[next_pos] = cur_pos

            if next_pos == target:
                print(visited[next_pos]) 
                print_path(prev_path, target)
                return
            
def print_path(prev_path, target):
    output = []

    while target != -1:
        output.append(target)
        target = prev_path[target]
    print(*output[::-1])



n, k = map(int, input().split())
bfs(n, k)