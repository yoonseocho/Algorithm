import sys
from itertools import permutations

input = sys.stdin.readline

def solution():
    ops = []
    for i, cnt in enumerate(op_list):
        if i == 0:
            ops += ['+'] * cnt
        elif i == 1:
            ops += ['-'] * cnt
        elif i == 2:
            ops += ['*'] * cnt
        else:
            ops += ['/'] * cnt
    op_perms = set(permutations(ops))
    
    results = []

    for op_seq in op_perms:
        result = num_list[0]
        for i in range(1, n):
            if op_seq[i - 1] == '+':
                result += num_list[i]
            elif op_seq[i - 1] == '-':
                result -= num_list[i]
            elif op_seq[i - 1] == '*':
                result *= num_list[i]
            if op_seq[i - 1] == '/':
                if result < 0:
                    result = -(-result // num_list[i])
                else:
                    result //= num_list[i]
                
        results.append(result)
    print(max(results))
    print(min(results))
        
n = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

solution()