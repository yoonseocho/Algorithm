from collections import deque

sentence = input()
stack = []
dq = deque()
flag = False

for s in sentence:
    if s == "<":
        if stack:
            for _ in range(len(stack)):
                print(stack.pop(), end='')
        flag = True
        dq.append(s)
    elif s == ">":
        flag = False
        dq.append(s)
        for _ in range(len(dq)):
            print(dq.popleft(), end='')
    elif flag == True:
        dq.append(s)
    elif s == " ":
        for _ in range(len(stack)):
            print(stack.pop(), end='')
        print(" ", end='')
    else:
        stack.append(s)

for _ in range(len(stack)):
    print(stack.pop(), end='')