def solution(prices):
    n = len(prices)
    answer = [0] * n
    stk = []
    
    for curr_idx, price in enumerate(prices):
        while stk and prices[stk[-1]] > price:
            prev_idx = stk.pop()
            answer[prev_idx] = curr_idx - prev_idx
        stk.append(curr_idx)
    
    while stk:
        prev_idx = stk.pop()
        answer[prev_idx] = (n-1) - prev_idx
    
    return answer
        