from itertools import permutations

x = list(input().strip())

cases = list(permutations(x, len(x)))
nums = []
for case in cases:
    num = int(''.join(case))
    nums.append(num)
nums = list(set(nums))
nums.sort()
for i in range(len(nums)-1):
    if nums[i] == int(''.join(x)):
        print(nums[i+1])
        break
else:
    print(0)