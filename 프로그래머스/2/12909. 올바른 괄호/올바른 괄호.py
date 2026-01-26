def solution(s):
    stk = []
    
    for char in s:
        if stk and char == ")":
            stk.pop()
        else:
            stk.append("(")
    
    return False if stk else True