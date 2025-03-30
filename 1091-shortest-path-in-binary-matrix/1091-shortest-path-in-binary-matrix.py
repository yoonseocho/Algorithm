from collections import deque

class Solution:
   def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortest_path_len = -1

        if grid[0][0] != 0:
            return shortest_path_len

        delta = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        row = len(grid)
        col = len(grid[0])

        visited = [[False] * col for _ in range(row)]

        q = deque()
        q.append((0, 0, 1))
        visited[0][0] = True

        while q:
            x, y, cur_len = q.popleft()

            if x == row - 1 and y == col - 1:
                shortest_path_len = cur_len
                break

            for dx, dy in delta:
                next_x = x + dx
                next_y = y + dy

                if 0 <= next_x < row and 0 <= next_y < col:
                    if grid[next_x][next_y] == 0 and visited[next_x][next_y] == False:
                        visited[next_x][next_y] == True
                        q.append((next_x, next_y, cur_len + 1))
                    
        return shortest_path_len

