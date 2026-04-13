import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().strip().split())
DNAs = []
for _ in range(N):
    DNA = input().strip()
    DNAs.append(DNA)

s = ""
total_dist = 0
for col in zip(*DNAs):
    counts = Counter(col)
    
    best = max(sorted(counts.keys()), key=counts.get)
    s += best

    total_dist += N - counts[best]

print(s)
print(total_dist)



