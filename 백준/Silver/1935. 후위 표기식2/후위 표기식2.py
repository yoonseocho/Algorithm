import sys

input = sys.stdin.read

data = input().splitlines()

N = int(data[0])
postfix = data[1]

stack = []
nums = {}
for i in range(N):
    char = chr(ord('A') + i)
    nums[char] = int(data[2+i])

for p in postfix:
    if p in ['+', '-', '*', '/']:
        a = stack.pop()
        b = stack.pop()
        if p == "+":
            b += a
        elif p == "-":
            b -= a
        elif p == "*":
            b *= a
        elif p == "/":
            b /= a
        stack.append(b)
    else:
        stack.append(nums[p])
    
print(f"{stack[0] :.2f}")