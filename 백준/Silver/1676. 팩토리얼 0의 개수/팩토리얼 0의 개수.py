def factorial(x):
    if x == 1 or x == 0:
        return 1
    return x * factorial(x-1)

N = int(input())
count = 0

num = str(factorial(N))

for i in num[::-1]:
    if i == "0":
        count += 1
    else:
        break
print(count)