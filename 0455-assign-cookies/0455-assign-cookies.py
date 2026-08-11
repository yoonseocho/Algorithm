class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        cnt = 0

        g.sort()
        s.sort()

        i = 0
        for cookie in s:
            if i < n and cookie >= g[i]:
                i += 1
        return i


        