import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    ps = input().rstrip()
    stk = []
    valid = True
    for i in ps:
        if i == "(":
            stk.append(")")
        elif stk and stk[-1] == i:
            stk.pop()
        else:
            valid = False
            break
        
    print("YES" if valid and not stk else "NO")
