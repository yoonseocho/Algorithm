import sys
import math

input = sys.stdin.readline

n,m = map(int, input().strip().split(":"))

num = math.gcd(n, m)

print(f"{n//num}:{m//num}")
