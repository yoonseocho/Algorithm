class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. whitespace
        s = s.lstrip()
        if not s:
            return 0

        # 2. signedness
        sign = 1
        idx = 0

        if s[idx] == "-":
            sign = -1
            idx += 1
        elif s[idx] == "+":
            idx += 1
        
        # 3. conversion
        start_idx = idx
        while idx < len(s) and s[idx].isdigit():
            idx += 1
        
        if start_idx == idx:
            return 0

        # 4. rounding
        num = sign * int(s[start_idx: idx])

        if -2**31 <= num <= 2**31 - 1:
            return num
        elif num < -2**31:
            return -2**31
        else:
            return 2**31 - 1