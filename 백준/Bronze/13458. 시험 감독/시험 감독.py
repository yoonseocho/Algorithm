import sys

input = sys.stdin.readline

def solution():
    total_supervisor = 0
    for i in range(len(num_list)):
        if num_list[i] - b > 0:
            num_list[i] -= b
            if num_list[i] % c == 0:
                total_supervisor = total_supervisor + 1 + (num_list[i] // c)
            else:
                total_supervisor = total_supervisor + 2 + (num_list[i] // c)
        else:
            total_supervisor += 1

    return total_supervisor

n = int(input())

num_list = list(map(int, input().split()))

b, c = map(int, input().split())

print(solution())