import sys

input = sys.stdin.read
data = input().splitlines()
result = sorted(data[1:], key = lambda x: tuple(map(int, x.split())))
print('\n'.join(result))