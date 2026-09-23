class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memo = {}
        for idx, num in enumerate(nums):
            if target - num in memo:
                return [idx, memo[target - num]]
            else:
                memo[num] = idx