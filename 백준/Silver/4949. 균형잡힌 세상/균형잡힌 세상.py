import sys

input = sys.stdin.readline

while True:
    ps = input().rstrip()
    stk = []
    valid = True
    if ps == ".":
        break

    for i in ps:
        if i == "(":
            stk.append(")")
        elif i == "[":
            stk.append("]")
        elif i == ")" or i == "]":
            if stk and stk[-1] == i:
                stk.pop()
            else:
                valid = False
                break
    print("yes" if valid and not stk else "no")