import sys
input = sys.stdin.readline
string = input().rstrip()
left_stack = list(string)
right_stack = []

for _ in range(int(input().rstrip())):
    cmd = input().rstrip().split()
    if cmd[0] == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    elif cmd[0] == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    elif cmd[0] == "B":
        if left_stack:
            left_stack.pop()
    elif cmd[0] == "P":
        left_stack.append(cmd[1])

print(''.join(left_stack+list(reversed(right_stack))))