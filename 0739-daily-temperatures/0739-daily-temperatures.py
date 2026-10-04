class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stk = []

        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                prev_idx = stk.pop()
                answer[prev_idx] = i - prev_idx
            stk.append(i)

        return answer