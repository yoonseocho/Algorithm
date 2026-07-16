from collections import deque

def solution(game_board, table):
    def extract_blocks(board, target):
        n = len(board)
        visited = [[False] * n for _ in range(n)]
        blocks = []
        
        dxs = [-1, 1, 0, 0]
        dys = [0, 0, -1, 1]
        
        def in_range(x, y):
            return 0<=x<n and 0<=y<n
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == target and not visited[i][j]:
                    # bfs 시작
                    q = deque([(i, j)])
                    visited[i][j] = True
                    
                    block_coords = [(i, j)]
                    
                    while q:
                        x, y = q.popleft()
                        
                        for dx, dy in zip(dxs, dys):
                            nx, ny = x + dx, y + dy
                            
                            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == target:
                                q.append((nx, ny))
                                visited[nx][ny] = True
                                block_coords.append((nx, ny))
                    
                    blocks.append(block_coords)
        return blocks
        
    
    def align_origin(block):
        min_x = min(b[0] for b in block)
        min_y = min(b[1] for b in block)

        normalized_block = [(x-min_x, y-min_y) for x, y in block]

        return sorted(normalized_block)
        
    
    def rotate_block(block):
        rotated_block = [(y, -x) for x, y in block]
        return align_origin(rotated_block)
    
    # 들어맞는지 비교
    blank_pieces = [align_origin(blank_piece) for blank_piece in extract_blocks(game_board, 0)]
    puzzle_pieces = [align_origin(puzzle_piece) for puzzle_piece in extract_blocks(table, 1)]
    
    used_puzzle = [False] * len(puzzle_pieces)
    answer = 0
    
    for blank in blank_pieces:
        for i, puzzle in enumerate(puzzle_pieces):
            if used_puzzle[i]:
                continue
            
            if len(blank) != len(puzzle):
                continue
            
            match_found = False
            rotated = puzzle
            
            for _ in range(4):
                if blank == rotated:
                    match_found = True
                    break
                rotated = rotate_block(rotated)
            
            if match_found:
                used_puzzle[i] = True
                answer += len(blank)
                break
    return answer
        
    
                    
    
    
    
    
    
    
    