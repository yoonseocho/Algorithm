import sys

input = sys.stdin.readline

stack = []
result = []
current = 1

for _ in range(int(input().rstrip())):
    num = int(input().rstrip())
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
else:
    print('\n'.join(result))