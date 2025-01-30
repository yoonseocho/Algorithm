N = int(input())
nums = list(map(int, input().split()))
tmp = 0
count = 0

for num in nums:
    tmp = 0
    for i in range(1, num):
        if num / i == num // i:
            tmp += 1
    if tmp == 1:
        count += 1
print(count)