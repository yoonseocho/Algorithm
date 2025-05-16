def solution(s):
    stk = []
    
    for p in s:
        if p == "(":
            stk.append(p)
        elif p == ")":
            if stk:
                stk.pop()
            else:
                return False
    return len(stk) == 0