import sys
from collections import Counter

input = sys.stdin.readline

def palindrome():
    S = input().strip()

    if S == S[::-1]:
        return len(S)

    for i in range(1, len(S)):
        if S[i:] == S[i:][::-1]:
            p = S + S[:i][::-1]
            return len(p)
print(palindrome())