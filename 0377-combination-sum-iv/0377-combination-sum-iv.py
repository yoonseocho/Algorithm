class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        nums.sort()

        for i in range(1, target+1):
            for num in nums:
                diff = i - num
                if diff < 0:
                    break
                dp[i] += dp[diff]
        return dp[-1]