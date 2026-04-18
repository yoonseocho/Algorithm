from itertools import combinations

n, m = map(int, input().split())

nums = [num for num in range(1, n+1)]

cases = combinations(nums, m)

for case in cases:
    print(*case)
