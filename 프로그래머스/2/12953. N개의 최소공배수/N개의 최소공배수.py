import math

def lcm(a, b):
    gcd = math.gcd(a, b)
    return gcd * (a//gcd) * (b//gcd)

def solution(arr):
    arr.sort()
    tmp_lcm = arr[0]
    for i in range(1, len(arr)):
        tmp_lcm = lcm(tmp_lcm, arr[i])
    return tmp_lcm
        