import sys
input = sys.stdin.readline
N = int(input().rstrip())
count = N

for _ in range(N):
    word = input().rstrip()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i+1] in word[:i]:
                count -= 1
                break
print(count)