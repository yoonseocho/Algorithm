class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = {}
        for char in s:
            if char not in memo:
                memo[char] = 1
            else:
                memo[char] += 1
        
        for idx, char in enumerate(s):
            if memo[char] == 1:
                return idx
        return -1