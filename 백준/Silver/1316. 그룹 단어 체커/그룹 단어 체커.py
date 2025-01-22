import sys
input = sys.stdin.readline
count = 0

for _ in range(int(input().rstrip())):
    word = input().rstrip()
    if list(word) == sorted(word, key=word.find):
        count += 1
print(count)