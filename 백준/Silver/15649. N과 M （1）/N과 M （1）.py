n, m = map(int, input().split())

path = []
visited = [False] * (n+1)
def backtracking(depth):
    #print(f"ENTER: depth={depth}, path={path}")
    if depth == m:
        print(*path)
        #print(" >>> 완료! 저장: {path}")
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            path.append(i)

            backtracking(depth+1)

            path.pop()
            visited[i] = False
            #print(f"BACK: depth={depth}, path={path}")

backtracking(0)
