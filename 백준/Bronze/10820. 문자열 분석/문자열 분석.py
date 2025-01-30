import sys

input = sys.stdin.read

data = input().splitlines()

for sentence in data:
    output = [0] * 4
    for s in sentence:
        if s.islower():
            output[0] += 1
        elif s.isupper():
            output[1] += 1
        elif s.isdigit():
            output[2] += 1
        else:
            output[3] += 1
    print(*output)
