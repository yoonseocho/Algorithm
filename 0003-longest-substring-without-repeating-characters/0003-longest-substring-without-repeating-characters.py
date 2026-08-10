class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        max_len = 0

        for idx, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= start:
                start = last_seen[ch] + 1
            last_seen[ch] = idx
            max_len = max(max_len, idx-start+1)
        return max_len