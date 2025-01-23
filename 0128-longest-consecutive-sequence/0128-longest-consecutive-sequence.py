class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        max_count = 0
        
        for num in nums:
            nums_dict[num] = True
        
        for num in nums_dict:
            if num - 1 not in nums_dict:
                cnt = 1
                target = num + 1
                while target in nums_dict:
                    cnt += 1
                    target += 1
                max_count = max(max_count, cnt)
        return max_count