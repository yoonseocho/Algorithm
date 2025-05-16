def solution(s):
    stk = []
    
    for p in s:
        if stk and stk[-1] != p:
            stk.pop()
        else:
            stk.append(p)
            if stk[0] == ")":
                return False
    if stk:
        return False
    else:
        return True