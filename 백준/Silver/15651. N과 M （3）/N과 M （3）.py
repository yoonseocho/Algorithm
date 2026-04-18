n, m = map(int, input().split())

path = []
def backtracking(depth):
    if depth == m:
        print(*path)
        return
    
    for i in range(1, n+1):
        path.append(i)

        backtracking(depth+1)

        path.pop()

backtracking(0)