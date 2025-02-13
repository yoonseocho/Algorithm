from collections import deque

class Solution:
    def climbStairs(self, n: int) -> int:
        q = deque()
        q.append(n)
        count = 0

        while q:
            cur_pos = q.popleft()
        
            for next_pos in (cur_pos-1, cur_pos-2):
                if next_pos == 0:
                    count += 1
                elif next_pos > 0:
                    q.append(next_pos)
        return count
            