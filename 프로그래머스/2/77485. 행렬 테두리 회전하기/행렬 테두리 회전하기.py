def solution(rows, columns, queries):
    board = [[0] * columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = num
            num += 1
    
    answer = []
            
    for query in queries:
        r1, c1, r2, c2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        
        temp = board[r1][c1]
        min_val = temp
        
        # 왼쪽 테두리: 아래에서 위로
        for i in range(r1, r2):
            board[i][c1] = board[i+1][c1]
            min_val = min(min_val, board[i][c1])
                
        # 아래쪽 테두리: 오른쪽에서 왼쪽으로
        for j in range(c1, c2):
            board[r2][j] = board[r2][j+1]
            min_val = min(min_val, board[r2][j])
        
        # 오른쪽 테두리: 위에서 아래로
        for i in range(r2, r1, -1):
            board[i][c2] = board[i-1][c2]
            min_val = min(min_val, board[i][c2])
        
        # 위쪽 테두리: 왼쪽에서 오른쪽으로
        for j in range(c2, c1, -1):
            board[r1][j] = board[r1][j-1]
            min_val = min(min_val, board[r1][j])
            
        board[r1][c1+1] = temp
        answer.append(min_val)
    return answer