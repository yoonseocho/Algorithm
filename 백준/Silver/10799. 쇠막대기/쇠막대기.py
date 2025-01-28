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
        if prev == "(":
            count -= 1
            count += len(stack)-1
        stack.pop()
    prev = p

print(count)