def solution(arr):
    stk = []
    
    for num in arr:
        if stk and stk[-1] == num:
            continue
        else:
            stk.append(num)
    return stk
        
            