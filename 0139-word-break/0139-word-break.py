class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(curr_s):
            if curr_s == "":
                return True

            if curr_s in memo:
                return memo[curr_s]
            
            for word in wordDict:
                if curr_s.startswith(word):
                    next_s = curr_s[len(word):]
                    if dfs(next_s):
                        memo[curr_s] = True
                        return True

            memo[curr_s] = False
            return False

        return dfs(s)