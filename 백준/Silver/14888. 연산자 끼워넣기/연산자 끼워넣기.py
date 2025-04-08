import sys

input = sys.stdin.readline

max_val = -float('inf')
min_val = float('inf')

def dfs(idx, result):
    global max_val, min_val

    if idx == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    for i in range(4):
        if op_list[i] > 0:
            op_list[i] -= 1

            if i == 0:
                next_result = result + num_list[idx]
            elif i == 1:
                next_result = result - num_list[idx]
            elif i == 2:
                next_result = result * num_list[idx]
            elif i == 3:
                if result < 0:
                    next_result = -(-result // num_list[idx])
                else:
                    next_result = result // num_list[idx]

            dfs(idx + 1, next_result)
            op_list[i] += 1


        
n = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

dfs(1, num_list[0])
print(max_val)
print(min_val)