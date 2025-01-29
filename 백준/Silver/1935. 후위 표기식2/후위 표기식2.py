N = int(input())
postfix = input()

stack = []
nums = {}
for i in range(N):
    char = chr(ord('A') + i)
    nums[char] = int(input())

for p in postfix:
    if p == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif p == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif p == "*":
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif p == "/":
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    else:
        stack.append(nums[p])
    
print(f"{stack[-1] :.2f}")