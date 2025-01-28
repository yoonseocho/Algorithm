import sys

input = sys.stdin.read
data = input().splitlines()

nums = list(map(int, " ".join(data[1:]).split()))
stack = []
answer = [-1] * int(data[0])

for idx, num in enumerate(nums):
    while stack and stack[-1][1] < num:
        temp_idx = stack.pop()[0]
        answer[temp_idx] = num
    stack.append((idx, num))
print(*answer)