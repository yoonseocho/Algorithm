import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


N = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    if is_prime(num):
        count += 1
print(count)