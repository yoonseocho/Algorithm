class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        answer = [intervals[0]]

        for start, end in intervals[1:]:
            if answer[-1][1] >= start:
                prev_start, prev_end = answer.pop()
                answer.append([min(prev_start, start), max(prev_end, end)])
            else:
                answer.append([start, end])
        
        return answer