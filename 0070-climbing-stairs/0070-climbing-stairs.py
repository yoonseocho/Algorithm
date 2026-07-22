class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        if n == 1 or n == 2:
            return memo[n]

        for i in range(3, n+1):
            memo[i] = memo[i-2] + memo[i-1]
        
        return memo[n]