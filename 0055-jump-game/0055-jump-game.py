class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        dp = [False] * n

        for i, num in enumerate(nums):
            if num == 0:
                for k in range(i+1, n):
                    if dp[k]:
                        break
                else:
                    return False
            for j in range(i+1, i+num+1):
                if j < n:
                    dp[j] = True
                if dp[n-1]:
                    return True
        print(dp)
        return dp[n-1]