class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top, bottom, left, right = 0, m-1, 0, n-1
        answer = []

        while top <= bottom and left <= right:
            # 왼 -> 오
            for i in range(left, right+1):
                answer.append(matrix[top][i])
            top += 1
            print(answer)

            # 위 -> 아래
            for i in range(top, bottom+1):
                answer.append(matrix[i][right])
            right -= 1
            print(answer)

            # 오 -> 왼
            if top <= bottom:
                for i in range(right, left-1, -1):
                    answer.append(matrix[bottom][i])
                bottom -= 1
                print(answer)

            # 아래 -> 위
            if left <= right:
                for i in range(bottom, top-1, -1):
                    answer.append(matrix[i][left])
                left += 1
            print(answer)
        return answer