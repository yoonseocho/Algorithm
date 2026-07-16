class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        
        rev_num = sign * int(str(abs(x))[::-1])

        if -2**31 <= rev_num <= 2**31 - 1:
            return rev_num
        else:
            return 0