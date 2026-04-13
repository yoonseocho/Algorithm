import sys

input = sys.stdin.readline

word = input().strip()
N = int(input().strip())
cnt = 0
for _ in range(N):
    ring = input().strip()
    if word in ring+ring:
        cnt += 1
print(cnt)
