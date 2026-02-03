def solution(s):
    stk = []
    
    for char in s:
        if stk and stk[-1] == char:
            stk.pop()
            continue
        stk.append(char)
    return 1 if not stk else 0