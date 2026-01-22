def explore_row(grid):
    cnt = 0
    for row in grid:
        if all(char=="#" for char in row):
            cnt += 1
    return cnt

def explore_column(H, W, grid):
    cnt = 0
    for j in range(W):
            if all(grid[i][j] == "#" for i in range(H)):
                cnt += 1
    return cnt



T = int(input())
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    
    grid = [list(input()) for _ in range(H)]
    cnt = 0
    
    row_cnt = explore_row(grid)
    col_cnt = explore_column(H, W, grid)
    
    if row_cnt == H and col_cnt == W:
        ans = min(H, W)
    else:
        ans = row_cnt + col_cnt
    
    print(ans)
                
                
    