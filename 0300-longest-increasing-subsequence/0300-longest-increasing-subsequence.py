class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            max_num = 0
            for j in range(n):
                if nums[i] > nums[j]:
                    max_num = max(max_num, dp[j])
            dp[i] = max_num + 1
        
        # print(dp)
        return max(dp)