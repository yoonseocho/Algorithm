import sys

input = sys.stdin.readline

N = int(input().strip())

unique_groups = []
for _ in range(N):
    current_word = input().strip()

    is_cyclic = False

    for existing_word in unique_groups:
        if len(current_word) == len(existing_word) and current_word in (existing_word+existing_word):
            is_cyclic = True
            break

    if not is_cyclic:
        unique_groups.append(current_word)

print(len(unique_groups))