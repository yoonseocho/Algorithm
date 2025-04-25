class Solution:
    def reverse(self, x: int) -> int:  
        if x > 0:
            sign = 1
        else:
            sign = -1

        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1:
                return 0
        return sign * rev
                
        
        
        