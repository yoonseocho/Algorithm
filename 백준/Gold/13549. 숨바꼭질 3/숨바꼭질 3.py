from collections import deque

def bfs(start, target):
    if start == target:
        return 0
    visited = [-1] * 100001
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur_pos = q.popleft()

        teleportation = cur_pos * 2
        if 0 <= teleportation <= 100000 and visited[teleportation] == -1:
            q.append(teleportation)
            visited[teleportation] = visited[cur_pos]
        if teleportation == target:
            return visited[teleportation]

        for next_pos in (cur_pos - 1, cur_pos + 1):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                q.append(next_pos)
                visited[next_pos] = visited[cur_pos] + 1
            if next_pos == target:
                return visited[next_pos]
        

n, k = map(int, input().split())
print(bfs(n, k))