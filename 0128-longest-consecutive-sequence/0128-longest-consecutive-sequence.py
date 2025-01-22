class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {}
        count = 0
        max_count = 0
        for num in nums:
            num_dict[num] = True
        for num in num_dict:
            if num-1 not in num_dict:
                count = 1
                target = num + 1
                while target in num_dict:
                    target += 1
                    count += 1
                max_count = max(max_count, count)
        return max_count

            