def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stk = [] # 인덱스를 저장
    
    for i in range(n):
        while stk and numbers[stk[-1]] < numbers[i]:
            answer[stk.pop()] = numbers[i]
        stk.append(i)
    
    return answer