def solution(clothes):
    memo = {}
    
    for _, category in clothes:
        if category in memo:
            memo[category] += 1
        else:
            memo[category] = 1
    
    answer = 1
    for val_cnt in memo.values():
        answer *= val_cnt + 1
    return answer - 1
        
    
        
        