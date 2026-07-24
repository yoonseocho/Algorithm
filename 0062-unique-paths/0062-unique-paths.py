class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1

        if m < 2 or n < 2:
            return 1

        grid[0][1], grid[1][0] = 1, 1

        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or (i == 0 and j == 1) or (i == 1 and j == 0):
                    continue
                from_top = grid[i-1][j]
                from_left = grid[i][j-1]
                grid[i][j] = from_top + from_left
        return grid[m-1][n-1]
                