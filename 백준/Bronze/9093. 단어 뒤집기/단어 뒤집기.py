for _ in range(int(input())):
    sentence = list(map(str, input().split()))
    for i in sentence:
        print(''.join(reversed(i)), end = " ")
    print()