class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        answer = [intervals[0]]

        for s, e in intervals[1:]:
            if s <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], e)
            else:
                answer.append([s, e])
        return answer