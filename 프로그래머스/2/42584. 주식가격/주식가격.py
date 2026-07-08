def solution(prices):
    ans = [0] * len(prices)
    stk = []
    
    for idx, price in enumerate(prices):
        while stk and stk[-1][1] > price:
            prev_idx, _ = stk.pop()
            ans[prev_idx] = idx - prev_idx
        stk.append((idx, price))
    
    # 끝까지 안떨어진 것들
    max_time = len(prices) - 1
    while stk:
        prev_idx, _ = stk.pop()
        ans[prev_idx] = idx - prev_idx
    return ans
    
    