import sys

stack = []
count = 0

parentheses = sys.stdin.readline()

prev = ""
for p in parentheses:
    if p == "(":
        stack.append(")")
        count += 1
    elif stack and stack[-1] == p:
        if prev == "(": # 레이저인 경우
            stack.pop()
            count -= 1
            count += len(stack)
        else: # 막대기의 끝
            stack.pop() 
    prev = p

print(count)