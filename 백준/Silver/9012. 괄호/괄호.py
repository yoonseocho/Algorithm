import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    ps = input().rstrip()
    stk = []
    valid = True
    for i in ps:
        if i == "(":
            stk.append(")")
        elif i == ")":
            if stk and stk[-1] == ")":
                stk.pop()
            else:
                valid = False
                break
    if valid and not stk:
        print("YES")
    else:
        print("NO")