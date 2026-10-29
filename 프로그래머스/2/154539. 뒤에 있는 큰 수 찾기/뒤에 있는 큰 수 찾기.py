def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stk = []
    
    for idx, number in enumerate(numbers):
        while stk and stk[-1][1] < number:
            prev_idx, prev_num = stk.pop()
            answer[prev_idx] = number
        stk.append((idx, number))
    
    return answer