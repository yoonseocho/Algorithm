from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        visited = [-1] * 10001
        prev = [-1] * 10001
        min_steps = float('inf')

        
        q = deque()
        q.append(amount)
        visited[amount] = 0

        while q:
            cur_pos = q.popleft()

            if visited[cur_pos] > min_steps:
                break

            for i in coins:
                next_pos = cur_pos - i
                if 0 <= next_pos <= 10000 and visited[next_pos] == -1:
                    prev[next_pos] = cur_pos
                    visited[next_pos] = visited[cur_pos] + 1
                    q.append(next_pos)

                    if next_pos == 0:
                        min_steps = visited[next_pos]
        output = [-1]
        temp = prev[0]
        while temp != -1:
            output.append(temp)
            temp = prev[temp]
        if output[-1] == -1:
            return -1
        else:
            return (len(output)-1)