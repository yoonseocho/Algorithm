from itertools import product

n, m = map(int, input().split())

nums = [num for num in range(1, n+1)]

cases = product(nums, repeat=m)

for case in cases:
    print(*case)
