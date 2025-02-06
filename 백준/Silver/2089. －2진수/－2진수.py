n = int(input())

output = []

if n == 0:
    print(0)
    exit()

while n:
    if n % (-2):
        output.append(1)
        n = n // (-2) + 1
    else:
        output.append(0)
        n = n // (-2)

print(''.join(map(str, output[::-1])))