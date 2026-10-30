class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stk = []
        answer = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stk and stk[-1][1] < temp:
                prev_idx, _ = stk.pop()
                answer[prev_idx] = idx - prev_idx
            stk.append((idx, temp))
        
        return answer