class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in memo:
                return [memo[complement], i]
            memo[num] = i
