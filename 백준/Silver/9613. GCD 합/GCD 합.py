import math
from itertools import combinations
import sys

input = sys.stdin.read

data = input().splitlines()

n = int(data[0])

for i in range(1, n+1):
    test_case = list(map(int, data[i].split()))
    result = sum(math.gcd(a,b) for a, b in combinations(test_case[1:], 2))
    print(result)