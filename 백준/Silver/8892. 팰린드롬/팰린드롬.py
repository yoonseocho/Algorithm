import sys

input = sys.stdin.readline

def is_palindrome(word):
    return word == word[::-1]

def check():
    K = int(input().strip())
    words = [input().strip() for _ in range(K)]

    for i in range(K):
        for j in range(K):
            if i == j:
                continue
            combined = words[i] + words[j]
            if is_palindrome(combined):
                return combined
    return 0
            
def solution():
    T = int(input().strip())

    for _ in range(T):
        print(check())

solution()

