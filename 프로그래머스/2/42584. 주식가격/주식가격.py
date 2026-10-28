def solution(prices):
    n = len(prices)
    answer = [0] * n
    stk = []
    
    for idx, price in enumerate(prices):
        while stk and stk[-1][1] > price:
            prev_idx, _ = stk.pop()
            answer[prev_idx] = idx - prev_idx
        stk.append((idx, price))
    
    while stk:
        idx, price = stk.pop()
        answer[idx] = (n-1) - idx
    
    return answer