def solution(n):
    cnt = bin(n)[2:].count('1')
    new_cnt = -1
    while cnt != new_cnt:
        n += 1
        new_cnt = bin(n)[2:].count('1')
    return n
    