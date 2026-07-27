class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        dp1 = [0] * (n+1)
        dp2 = [0] * (n+1)
        dp3 = [0] * (n+1)

        # case1. 첫집만 터는 경우
        dp1[1] = nums[0]
        dp1[2] = nums[0]
    
        for i in range(3, n):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i-1])

        dp1[n] = dp1[n-2]

        # case2. 끝집만 터는 경우
        dp2[1] = 0
        dp2[n] = nums[n-1]
        dp2[n-1] = dp2[n]

        for i in range(n-2, 1, -1):
            dp2[i] = max(dp2[i+1], dp2[i+2] + nums[i-1])

        # case3. 첫집 끝집 둘 다 안터는 경우
        dp3[1] = 0
        dp3[2] = nums[1]

        for i in range(3, n):
            dp3[i] = max(dp3[i-1], dp3[i-2] + nums[i-1])

        dp3[n] = dp3[n-2]

        return max(*dp1, *dp2, *dp3)