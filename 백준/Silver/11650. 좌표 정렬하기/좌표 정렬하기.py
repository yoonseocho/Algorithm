import sys

input = sys.stdin.readline
result = []

for _ in range(int(input().rstrip())):
    i  = list(map(int, input().rstrip().split()))
    result.append(i)

result.sort()

for i in result:
    print(' '.join(map(str, i)))
