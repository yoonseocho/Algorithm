from collections import Counter

def solution(want, number, discount):
    possible = 0
    target = dict(zip(want, number))
    memo = Counter(discount[:10])
    
    if memo == target:
        possible += 1
        
    for i in range(1, len(discount)-9):
        prev_item = discount[i-1]
        next_item = discount[i+9]
        
        memo[prev_item] -= 1
        if memo[prev_item] == 0:
            del memo[prev_item]
        
        memo[next_item] += 1
        
        if memo == target:
            possible += 1
    return possible