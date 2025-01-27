import sys

word = sys.stdin.readline().rstrip()
alphabet = [0] * 26

for i in word:
    alphabet[ord(i)-ord('a')] += 1

for i in alphabet:
    print(i, end=" ")