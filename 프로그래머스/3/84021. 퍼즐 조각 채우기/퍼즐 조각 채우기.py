from collections import deque

def solution(game_board, table):
    n = len(game_board)
    
    visited_board = [[False] * n for _ in range(n)]
    visited_table = [[False] * n for _ in range(n)]
    
    def in_range(r, c):
        return 0<= r < n and 0<= c < n
    
    def bfs(r, c, board, visited, num):
        q = deque([(r, c)])
        visited[r][c] = True
        drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
        piece = [(r, c)]
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                
                if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == num:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    piece.append((nr, nc))
        return piece
            
    def get_pieces(board, visited, num):
        pieces = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == num and not visited[i][j]:
                    piece = bfs(i, j, board, visited, num)
                    pieces.append(piece)
        return pieces
    
    def align_piece(piece):
        aligned_piece = []
        
        min_x = min(piece, key=lambda x: x[0])[0]
        min_y = min(piece, key=lambda x: x[1])[1]
        
        for x, y in piece:
            aligned_piece.append((x - min_x, y - min_y))
        
        return sorted(aligned_piece)
    
    def align_pieces(pieces):
        aligned_pieces = []
        for piece in pieces:
            aligned_piece = align_piece(piece)
            aligned_pieces.append(aligned_piece)
        
        return sorted(aligned_pieces)
            
    def get_blank_pieces_from_game_board():
        # 조각 뽑아내기
        pieces = get_pieces(game_board, visited_board, 0)
        
        # 정규화
        aligned_pieces = align_pieces(pieces)
        
        return aligned_pieces
    
    def get_puzzle_pieces_from_table():
        # 조각 뽑아내기
        pieces = get_pieces(table, visited_table, 1)
        
        # 정규화
        aligned_pieces = align_pieces(pieces)
        
        return aligned_pieces
    
    def rotate_piece(piece):
        # 시계방향 90도
        rotated_piece = [(c, -r) for r, c in piece]
        aligned_rotated_piece = align_piece(rotated_piece)
        
        return aligned_rotated_piece
            
    blank_pieces = get_blank_pieces_from_game_board()
    puzzle_pieces = get_puzzle_pieces_from_table()
    
    answer = 0
    
    # 사용된 퍼즐조각 제거
    used_puzzle = [False] * len(puzzle_pieces)
    
    for blank in blank_pieces:
        find = False
        for i, puzzle in enumerate(puzzle_pieces):
            if len(blank) != len(puzzle):
                continue
            if used_puzzle[i]:
                continue
                
            rotated_puzzle = puzzle
            
            for _ in range(4):
                rotated_puzzle = rotate_piece(rotated_puzzle)
                if blank == rotated_puzzle:
                    answer += len(blank)
                    find = True
                    used_puzzle[i] = True
                    break
            if find:
                break
    return answer
                    
    
    