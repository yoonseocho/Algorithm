import sys

input = sys.stdin.read

data = input().splitlines()

for sentence in data:
    l, u, d, b = 0, 0, 0, 0
    for s in sentence:
        if s.islower():
            l += 1
        elif s.isupper():
            u += 1
        elif s.isdigit():
            d += 1
        elif s.isspace():
            b += 1
    print(l, u, d, b)