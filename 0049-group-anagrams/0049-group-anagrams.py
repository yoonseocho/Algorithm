from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        memo = defaultdict(list)
        for each in strs:
            key = tuple(sorted(each))
            memo[key].append(each)
        
        return list(memo.values())