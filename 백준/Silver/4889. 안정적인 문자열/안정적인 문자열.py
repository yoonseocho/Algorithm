import sys

input = sys.stdin.readline

i = 1
while True:
    str_input = input().strip()
    if "-" in str_input:
        break
    
    stk = []
    for p in str_input:
        if stk and stk[-1] == "{" and p == "}":
            stk.pop()
        else:
            stk.append(p)
    
    cnt = 0
    while stk:
        p1 = stk.pop()
        p2 = stk.pop()

        if p1 == p2:
            cnt += 1
        else:
            cnt += 2
    print(f"{i}. {cnt}")
    i += 1