import sys

input = sys.stdin.readline

s = input().strip()
t = input().strip()

if s * len(t) == t * len(s):
    print(1)
else:
    print(0)

