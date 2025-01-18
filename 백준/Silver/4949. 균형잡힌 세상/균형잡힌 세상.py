import sys

input = sys.stdin.readline

while True:
    ps = input().rstrip()

    if ps == ".":
        break
    
    stk = []
    valid = True
    for i in ps:
        if i == "(":
            stk.append(")")
        elif i == "[":
            stk.append("]")
        elif i == ")" or i == "]":
            if stk and i == stk[-1]:
                stk.pop()
            else:
                valid = False
                break
    if valid and not stk:
        print("yes")
    else:
        print("no")
        
