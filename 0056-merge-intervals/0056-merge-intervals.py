class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        
        start, end = intervals[0][0], intervals[0][1]

        answer = []
        for s, e in intervals[1:]:
            if end >= s:
                end = max(end, e)
            else:
                answer.append([start, end])
                start, end = s, e
        answer.append([start, end])
        return answer