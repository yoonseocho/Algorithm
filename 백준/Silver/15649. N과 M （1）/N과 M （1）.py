from itertools import permutations

n, m = map(int, input().split())

nums = [num for num in range(1, n+1)]
cases = permutations(nums, m)

for p in cases:
    print(*p)