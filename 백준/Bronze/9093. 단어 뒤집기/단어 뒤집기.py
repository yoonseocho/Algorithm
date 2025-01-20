import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    text = input().rstrip()
    text_reversed = text[::-1].split()[::-1]
    print(' '.join(text_reversed))