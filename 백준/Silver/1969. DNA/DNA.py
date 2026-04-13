import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().strip().split())
DNAs = []
for _ in range(N):
    DNA = input().strip()
    DNAs.append(DNA)

best_char = []
for col in zip(*DNAs):
    counts = Counter(col)
    best = max(sorted(counts.keys()), key=counts.get)
    best_char.append(best)

s = ''.join(best_char)
cnt = 0
for a, s in zip(DNAs, [s]*len(DNAs)):
    for char_a, char_s in zip(a, s):
        if char_a != char_s:
            cnt += 1
print(s)
print(cnt)

