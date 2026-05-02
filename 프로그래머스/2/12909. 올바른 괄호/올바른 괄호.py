def solution(s):
    stk = []
    
    for p in s:
        if not stk and p == ")":
            return False
        if stk and p == ")":
            stk.pop()
        else:
            stk.append("(")
    return True if not stk else False