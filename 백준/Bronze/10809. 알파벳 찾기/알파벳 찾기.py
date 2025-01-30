word = input()

alphabet = [-1] * 26

for idx, val in enumerate(word):
    if alphabet[ord(val)-ord('a')] == -1:
        alphabet[ord(val)-ord('a')] = idx

print(*alphabet)