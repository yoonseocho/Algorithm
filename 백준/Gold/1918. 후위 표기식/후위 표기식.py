infix = input()

stack = []
answer = ""

for i in infix:
    if i == "(":
        stack.append(i)
    elif i == "*" or i == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            answer += stack.pop()
        stack.append(i)
    elif i == "+" or i == "-":
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.pop()
    else:
        answer += i
    
while stack:
    answer += stack.pop()

print(answer)