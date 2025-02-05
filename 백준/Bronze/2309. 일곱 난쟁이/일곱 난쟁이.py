import sys
from itertools import combinations

input = sys.stdin.read
data = list(map(int, input().rstrip().splitlines()))

for i in combinations(data, 7):
    if sum(i) == 100:
        print('\n'.join(map(str, sorted(i))))
        break
    