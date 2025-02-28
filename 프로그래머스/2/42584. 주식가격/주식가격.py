def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    for idx, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            prev_sec, _ = stack.pop()
            answer[prev_sec] = idx - prev_sec
        stack.append((idx, price))
    for idx, val in stack:
        answer[idx] = len(prices) - 1 - idx
    return answer