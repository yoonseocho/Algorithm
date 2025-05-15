class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        
        if x < 0:
            sign = -1
            
        x = abs(x)
        output = []
      
        while True:
            if x // 10 == 0:
                output.append(x % 10)
                break
            output.append(x % 10)
            x //= 10
            print(x)
        
        print(int(''.join(map(str, output))))
        reverse_x = sign * int(''.join(map(str, output)))
        
        if reverse_x > 2**31 or reverse_x < - 2**31:
            return 0
        else:
            return reverse_x
        