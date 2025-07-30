def solution(s):
    stk = []
    
    for char in s:
        if char == "(":
            stk.append(")")
        else:
            if stk:
                if stk[-1] == char:
                    stk.pop()
            else:
                return False
    return False if stk else True
            