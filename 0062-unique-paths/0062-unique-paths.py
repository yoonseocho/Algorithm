class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                from_top = grid[i-1][j]
                from_left = grid[i][j-1]
                grid[i][j] = from_top + from_left
        return grid[m-1][n-1]
                