n, m = map(int, input().split())

path = []
visited = [False] * (n+1)
def backtracking(start, depth):
    if depth == m:
        print(*path)
        return
    
    for i in range(start, n+1):
        if not visited[i]:
            visited[i] = True
            path.append(i)

            backtracking(i+1, depth+1)

            path.pop()
            visited[i] = False

backtracking(1, 0)