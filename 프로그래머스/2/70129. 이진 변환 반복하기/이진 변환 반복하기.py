def solution(s):
    cnt = 0
    length = 0
    zero_length = 0
    while length != 1:
        length = s.count('1')
        zero_length += len(s) - length
        s = bin(length)[2:]
        cnt += 1
    return [cnt, zero_length]