class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, val in enumerate(nums):
            complement = target - val
            if complement in hashmap:
                return [idx, hashmap[complement]]
            hashmap[val] = idx
            