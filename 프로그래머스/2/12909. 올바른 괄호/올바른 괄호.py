def solution(s):
    stk = []
    
    for char in s:
        if char == "(":
            stk.append("(")
        else:
            if not stk:
                return False
            stk.pop()
    
    return False if stk else True