import math
import sys

input = sys.stdin.read

data = input().splitlines()

n = int(data[0])

for i in range(1, n+1):
    test_case = list(map(int, data[i].split()))
    result = 0
    for j in range(1, len(test_case)-1):
        for k in range(j+1, len(test_case)):
            result += math.gcd(test_case[j], test_case[k])
    print(result)