import sys
input = sys.stdin.readline

count = [0] * 10001

for _ in range(int(input().rstrip())):
    num = int(input().rstrip())
    count[num] += 1

for i in range(1, 10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)