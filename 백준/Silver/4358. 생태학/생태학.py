import sys
from collections import Counter

input_datas = sys.stdin.read().splitlines()
words = [data for data in input_datas if data]

counts = Counter(words)
total = len(words)

for word in sorted(counts.keys()):
    ratio = (counts[word] / total) * 100
    print(f"{word} {ratio:.4f}")