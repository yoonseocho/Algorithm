class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        memo = {}

        for idx, num in sorted_nums:
            complement = target - num
            if complement in memo:
                return [memo[complement], idx]
            memo[num] = idx