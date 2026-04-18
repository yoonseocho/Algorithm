n = int(input().strip())
cnt = 0

v1 = [False] * n # 열
v2 = [False] * (2*n) # / 대각선
v3 = [False] * (2*n) # \ 대각선

def backtracking(row):
    global cnt
    if row == n:
        cnt += 1
        return
    
    for col in range(n):
        if not v1[col] and not v2[row+col] and not v3[row-col+n]:
            v1[col] = v2[row+col] = v3[row-col+n] = True

            backtracking(row + 1)

            v1[col] = v2[row+col] = v3[row-col+n] = False


backtracking(0)

print(cnt)