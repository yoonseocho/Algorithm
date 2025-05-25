def solution(s):
    stk = []
    
    for p in s:
        if p == "(":
            stk.append("(")
        else:
            if stk:
                stk.pop()
            else:
                return False
    return True if not stk else False