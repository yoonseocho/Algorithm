class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        dp1 = [0] * (n+1)
        dp2 = [0] * (n+1)

        # case1. 후보에서 첫집 제외
        dp1[2] = nums[1]
        dp1[3] = max(nums[1], nums[2])

        for i in range(3, n+1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i-1])

        # case2. 후보에서 끝집 제외
        dp2[1] = nums[0]
        dp2[2] = max(nums[0], nums[1])

        for i in range(3, n):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i-1])
        
        return max(*dp1, *dp2)