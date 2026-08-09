class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def in_range(r, c):
            return 0<=r<m and 0<=c<n

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            drs = [-1, 1, 0, 0]
            dcs = [0, 0, -1, 1]

            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc

                if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == word[idx]:
                    visited[nr][nc] = True
                    if dfs(nr, nc, idx+1):
                        return True
                    visited[nr][nc] = False
            return False
            


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(i, j, 1):
                        return True
                    visited[i][j] = False
        return False