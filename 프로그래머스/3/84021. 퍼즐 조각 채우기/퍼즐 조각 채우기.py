from collections import deque

def solution(game_board, table):
    n = len(game_board)
    
    def in_range(x, y):
        return 0<= x< n and 0<= y < n
    
    def extract_blocks(board, num):
        blocks = []
        visited = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == num and not visited[i][j]:
                    block = [(i, j)]
                    # bfs
                    q = deque([(i, j)])
                    visited[i][j] = True
                    
                    dxs = [-1, 1, 0, 0]
                    dys = [0, 0, -1, 1]
                    
                    while q:
                        x, y = q.popleft()
                        
                        for dx, dy in zip(dxs, dys):
                            nx, ny = x+dx, y+dy
                            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == num:
                                q.append((nx, ny))
                                visited[nx][ny] = True
                                block.append((nx, ny))
                    blocks.append(block)
        return blocks
    
    def align_origin(block):
        min_x = min([b[0] for b in block])
        min_y = min([b[1] for b in block])
        
        return sorted([(x-min_x, y-min_y) for x, y in block])
    
    def rotate(block):
        rotated_block = [(y, -x) for x, y in block]
        return align_origin(rotated_block)
    
    aligned_blank_pieces = sorted([align_origin(block) for block in extract_blocks(game_board, 0)])
    aligned_puzzle_pieces = sorted([align_origin(block) for block in extract_blocks(table, 1)])
    
    answer = 0
    used_blank = [False] * len(aligned_blank_pieces)
    for puzzle in aligned_puzzle_pieces:
        for idx, blank in enumerate(aligned_blank_pieces):
            if not used_blank[idx]:
                rotated_puzzle = puzzle
            
                for _ in range(4):
                    if rotated_puzzle == blank:
                        used_blank[idx] = True
                        answer += len(blank)
                        break
                    rotated_puzzle = rotate(rotated_puzzle)
                if used_blank[idx]:
                    break
    
    return answer
    
    
    
    
    