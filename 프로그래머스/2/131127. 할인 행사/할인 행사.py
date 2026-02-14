from collections import Counter

def solution(want, number, discount):
    possible = 0
    target = dict(zip(want, number))
    for i in range(len(discount)-9):
        memo = Counter(discount[i:i+10])
        if memo == target:
            possible += 1
    return possible