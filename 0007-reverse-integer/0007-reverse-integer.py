class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        num_list = []
        abs_x = abs(x)

        while abs_x:
            res = abs_x % 10
            abs_x //= 10
            num_list.append(res)

        num = int("".join(map(str, num_list)))

        if x < 0:
            num = -num
        if -2**31 <= num <= 2**31 - 1:
            return num
        else:
            return 0