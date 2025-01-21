import sys
input = sys.stdin.readline

word = input().rstrip()

l = 0
r = len(word)-1

while l<r:
    if word[l] != word[r]:
        print(0)
        break
    else:
        l += 1
        r -= 1
else:
    print(1)