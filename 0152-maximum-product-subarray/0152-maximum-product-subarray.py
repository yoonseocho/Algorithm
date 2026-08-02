class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(0, 0)] * n
        dp[0] = (nums[0], nums[0])
        
        for i in range(1, n):
            prev_min, prev_max = dp[i-1]
            candidates = (prev_min * nums[i], prev_max * nums[i], nums[i])
            dp[i] = (min(candidates), max(candidates))
        
        return max([t[1] for t in dp])