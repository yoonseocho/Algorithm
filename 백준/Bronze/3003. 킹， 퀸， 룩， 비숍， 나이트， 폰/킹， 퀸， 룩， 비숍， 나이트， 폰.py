answer = [1, 1, 2, 2, 2, 8]

white = list(map(int, input().split()))

result = [i-j for i, j in zip(answer, white)]

for i in result:
    print(i, end=" ")
