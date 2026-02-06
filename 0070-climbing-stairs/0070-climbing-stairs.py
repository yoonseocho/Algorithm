class Solution:
    memo = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n+1):
            self.memo[i] = self.memo[i-1] + self.memo[i-2]
        return self.memo[n]
