class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 열에 있는거 뒤집어서 행에 넣기
        cols = []
        for j in range(n):
            col = []
            for i in range(n):
                col.append(matrix[i][j])
            cols.append(col)
        
        for i, col in enumerate(cols):
            matrix[i][:] = col[::-1]