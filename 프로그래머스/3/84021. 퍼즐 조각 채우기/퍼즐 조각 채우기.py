from collections import deque

def solution(game_board, table):
    n = len(game_board)
    
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    q = deque()
    
    def in_range(x, y):
        return 0<=x<n and 0<=y<n
    
    def normalize(block):
        min_x = min(x for x, y in block)
        min_y = min(y for x, y in block)
        
        normalized_block = []
        for x, y in block:
            normalized_block.append((x-min_x, y-min_y))
            
        return sorted(normalized_block)
    
    def rotate(block):
        return [(y, -x) for x, y in block]
    
    def bfs(x, y, target_val, matrix, visited):
        block = []
        q.append((x, y))
        visited[x][y] = True
        
        while q:
            x, y = q.popleft()
            block.append((x, y))

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and not visited[nx][ny] and matrix[nx][ny] == target_val:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    
        return normalize(block)
                
                
    
    # game_board에서 0인 부분 추출
    visited_board = [[False] * n for _ in range(n)]
    board_pieces = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited_board[i][j]:
                piece = bfs(i, j, 0, game_board, visited_board)
                board_pieces.append(piece)
                
    # table에서 1인 부분 추출
    visited_table = [[False] * n for _ in range(n)]
    table_pieces = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited_table[i][j]:
                piece = bfs(i, j, 1, table, visited_table)
                table_pieces.append(piece)
    
    # game_board와 table 조각 비교
    table_used = [False] * len(table_pieces)
    answer = 0
    
    for board_p in board_pieces:
        found = False
        for i in range(len(table_pieces)):
            if table_used[i] or found:
                continue
            
            target_p = table_pieces[i]
            for _ in range(4):
                if board_p == target_p:
                    answer += len(board_p)
                    table_used[i] = True
                    found = True
                    break
                
                target_p = rotate(target_p)
                target_p = normalize(target_p)
            if found:
                break
    return answer
                
        