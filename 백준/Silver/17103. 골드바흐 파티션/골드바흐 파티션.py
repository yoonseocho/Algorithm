import math
import sys

def sieve(limit):
    prime_list = [True] * (limit+1)
    prime_list[0] = prime_list[1] = False

    for i in range(2, int(math.sqrt(limit))+1):
        if prime_list[i]:
            for j in range(i*i, limit+1, i):
                prime_list[j] = False
    return prime_list

LIMIT = 1000000
prime_bool = sieve(LIMIT)

data = sys.stdin.read().splitlines()
test_case = list(map(int, data[1:]))

for test in test_case:
    count = 0
    for i in range(1, test//2+1):
        if prime_bool[i] and prime_bool[test - i]:
            count += 1
    print(count)