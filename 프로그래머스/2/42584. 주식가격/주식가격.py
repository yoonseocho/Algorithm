def solution(prices):
    n = len(prices)
    answer = [0] * n
    stk = []
    
    for i in range(n):
        while stk and prices[stk[-1]] > prices[i]:
            prev_idx = stk.pop()
            answer[prev_idx] = i - prev_idx
        stk.append(i)
    
    # 스택에 남아있는것들
    for idx in stk:
        answer[idx] = (n-1) - idx
    
    return answer
    