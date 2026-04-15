import sys

input = sys.stdin.readline

n = int(input().strip())
enter = {}
for i in range(n):
    car = input().strip()
    enter[car] = i

exit_order = []
for _ in range(n):
    car = input().strip()
    exit_order.append(enter[car])

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if exit_order[i] > exit_order[j]:
            cnt += 1
            break
print(cnt)
