import sys

input = sys.stdin.readline

n,m = map(int, input().strip().split(":"))

def gcd(n, m):
    tmp = 1
    for i in range(2, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            tmp = i
    return tmp

num = gcd(n, m)

print(f"{n//num}:{m//num}")
