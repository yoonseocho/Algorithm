class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memo = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in memo:
                return [memo[complement], idx]
            memo[num] = idx