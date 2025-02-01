import math
import sys

def sieve(limit):
    prime_list = [True] * (limit + 1)
    prime_list[0] = prime_list[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime_list[i]:
            for j in range(i*i, limit+1, i):
                prime_list[j] = False
    return prime_list

LIMIT = 1000000
prime_bool = sieve(LIMIT)
prime_dict = {}

for i in range(2,LIMIT):
    if prime_bool[i]:
        prime_dict[i] = True

input = sys.stdin.readline

i = 0
while True:
    num = int(input().rstrip())
    if num == 0:
        break
    
    for p in prime_dict:
        if p > num // 2:
            break
        if num - p in prime_dict:
            print(f"{num} = {p} + {num - p}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
    
    i += 1
    
