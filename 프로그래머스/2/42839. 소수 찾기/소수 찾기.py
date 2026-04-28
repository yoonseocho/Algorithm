from itertools import permutations

def is_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    prime_num = set()
    for i in range(1, len(numbers)+1):
        cases = permutations(numbers, i)
    
        for case in cases:
            num = int(''.join(case))
            if is_prime(num):
                prime_num.add(num)
    return len(prime_num)