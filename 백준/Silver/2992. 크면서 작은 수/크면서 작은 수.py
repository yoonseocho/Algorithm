from itertools import permutations

X_str = input().strip()
X_int = int(X_str)

cases = sorted({int(''.join(p)) for p in permutations(X_str)})

result = 0
for n in cases:
    if n > X_int:
        result = n
        break
print(result)