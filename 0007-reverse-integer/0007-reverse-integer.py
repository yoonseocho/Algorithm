class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        
        if x < 0:
            sign = -1
            
        rev, x = 0, abs(x)

        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
        
        output = sign * rev
        
        if output > 2**31 or output < - 2**31:
            return 0
        else:
            return output
        