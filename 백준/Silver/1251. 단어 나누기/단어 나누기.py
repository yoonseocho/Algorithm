import sys

word = sys.stdin.readline().strip()
results = []
for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        part1 = word[:i]
        part2 = word[i:j]
        part3 = word[j:]

        combined = part1[::-1] + part2[::-1] + part3[::-1]
        results.append(combined)
results.sort()
print(results[0])