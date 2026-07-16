class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                common_prefix += chars[0]
            else:
                break
        
        return common_prefix