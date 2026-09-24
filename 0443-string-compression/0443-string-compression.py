class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        r, w = 0, 0

        while r < n:
            ch = chars[r]

            start = r
            while r < n and chars[r] == ch:
                r += 1
            count = r - start

            chars[w] = ch
            w += 1

            if count > 1:
                for d in str(count):
                    chars[w] = d
                    w += 1
            
        return w


