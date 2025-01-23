class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        longest = 0

        for num in nums:
            nums_dict[num] = True
        
        for num in nums_dict:
            if num-1 not in nums_dict:
                count = 1
                target = num + 1
                while target in nums_dict:
                    count += 1
                    target += 1
                longest = max(longest, count)
        return longest
            