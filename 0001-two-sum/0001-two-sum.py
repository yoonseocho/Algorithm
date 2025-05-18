class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            memo[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in memo and memo[complement] != i:
                return [i, memo[complement]]

            