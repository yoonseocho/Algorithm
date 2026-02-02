def remove_zeros(s, removed_zero):
    cnt = 0
    
    for num in s:
        if int(num) == 0:
            removed_zero += 1
            continue
        cnt += 1
    return cnt, removed_zero

def binary_num(num):
    if num == 1:
        return 1
    
    answer = []
    q = num
    res = 0
    
    while True:
        if q == 1:
            answer.append(1)
            break
        res = q % 2
        q = q // 2
        answer.append(res)
    
    return ''.join(map(str, answer[::-1]))

def solution(s):
    cnt = 0
    zero_length = 0
    length = 0
    while True:
        print(s, end=" ")
        if length == 1:
            break
        length, zero_length = remove_zeros(s, zero_length)
        s = binary_num(length)
        cnt += 1
        print(zero_length, length, s)
    return [cnt, zero_length]