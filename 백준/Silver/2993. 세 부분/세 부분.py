import sys

input = sys.stdin.readline

word = input().strip()
results = []
# 단어 세 부분으로 자르기

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        first, second, third = word[0:i], word[i:j], word[j:]
        combined = first[::-1] + second[::-1] + third[::-1]
        results.append(combined)

results.sort()
print(results[0])
