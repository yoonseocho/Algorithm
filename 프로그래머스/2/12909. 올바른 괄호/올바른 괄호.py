def solution(s):
    stk = []
    
    for char in s:
        if not stk and char == ")":
            return False
        elif stk and stk[-1] == char:
            stk.pop()
        elif char == "(":
            stk.append(")")
    return False if stk else True
            