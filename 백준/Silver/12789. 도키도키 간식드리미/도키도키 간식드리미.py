import sys

input = sys.stdin.readline
N = int(input().rstrip())
standing = list(map(int, input().rstrip().split()))

stk = []
current = 1

for s in standing:
    stk.append(s)
    while stk and stk[-1] == current:
        stk.pop()
        current += 1

print("Sad" if stk else "Nice")

