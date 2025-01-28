import sys
from collections import Counter

input = sys.stdin.read

data = input().splitlines()
nums = list(map(int, ' '.join(data[1:]).split()))

stack = []
answer = [-1] * int(data[0])
nums_ngf = [0] * int(data[0])

nums_freq = Counter(nums)

for i in range(len(nums)):
    nums_ngf[i] = nums_freq[nums[i]]

for idx, num in enumerate(nums_ngf):
    while stack and stack[-1][1] < num:
        temp_idx = stack.pop()[0]
        answer[temp_idx] = nums[idx]
    stack.append((idx, num))

print(*answer)