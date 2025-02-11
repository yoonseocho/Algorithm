from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortest_path_len = -1
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        if grid[0][0] != 0:
            return shortest_path_len
        
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        q = deque()
        q.append((0, 0, 1))
        visited[0][0] = True

        while q:
            cur_r, cur_c, cur_len = q.popleft()

            if cur_r == row - 1 and cur_c == col - 1:
                shortest_path_len = cur_len
                break

            for dx, dy in delta:
                next_r = cur_r + dx
                next_c = cur_c + dy
                if 0 <= next_r < row and 0 <= next_c < col:
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        q.append((next_r, next_c, cur_len + 1))
                        visited[next_r][next_c] = True

        return shortest_path_len
