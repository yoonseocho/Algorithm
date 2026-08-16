class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        idx = 0
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                idx = i
                break
        
        rotated_nums = nums[idx:] + nums[:idx]

        if sorted(nums) == rotated_nums:
            return True
        return False