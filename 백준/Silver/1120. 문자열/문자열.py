import sys

input = sys.stdin.readline

A, B = input().strip().split()

def get_diff(A, B):
    min_cnt = float('inf')
    for i in range(len(B)-len(A)+1):
        tmp_b = B[i:i+len(A)]
        cnt = 0
        for char_a, char_b in zip(A, tmp_b):
            if char_a != char_b:
                cnt += 1
        min_cnt = min(cnt, min_cnt)
    return min_cnt


print(get_diff(A, B))