for _ in range(int(input())):
    text = input()
    text_reversed = text[::-1].split()[::-1]
    print(' '.join(text_reversed))