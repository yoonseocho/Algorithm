def solution(s):
    stk = []
    
    for p in s:
        if p == "(":
            stk.append(p)
        elif p == ")":
            try:
                stk.pop()
            except:
                return False
    return len(stk) == 0