import sys

X_str = sys.stdin.readline().strip()
X_int = int(X_str)
n = len(X_str)

digit = list(X_str)
cases = []
path = []
visited = [False] * n
def backtracking(depth):
    #print(f"ENTER: depth={depth}, path={path}")
    if depth == n:
        cases.append(int(''.join(path)))
        #print(f" >>> 완성! 저장됨: {path}")
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            path.append(digit[i])

            backtracking(depth+1)

            path.pop()
            visited[i] = False
            #print(f"BACK: depth={depth}, path={path}")

backtracking(0)

sorted_nums = sorted(set(cases))
result = 0
for case in sorted_nums:
    if case > X_int:
        result = case
        break
print(result)
