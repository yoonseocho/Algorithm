import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())

def is_pangram(sentence):
    counts = Counter(sentence.lower())

    # 특수문자 제외 순수 알파벳만
    counts_list = []
    for i in range(26):
        alphabet = chr(ord('a') + i)
        counts_list.append(counts[alphabet])

    min_val = min(counts_list)
    if min_val == 1:
        return "ONE"
    elif min_val == 2:
        return "DOUBLE"
    elif min_val >= 3:
        return "TRIPLE"
    else:
        return "NONE"

for i in range(1, n+1):
    sentence = input().strip()
    result = is_pangram(sentence)
    if result == "ONE":
        print(f"Case {i}: Pangram!")
    elif result == "DOUBLE":
        print(f"Case {i}: Double pangram!!")
    elif result == "TRIPLE":
        print(f"Case {i}: Triple pangram!!!")
    else:
        print(f"Case {i}: Not a pangram")