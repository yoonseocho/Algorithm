string = input()
output = []

ROT13_dict = {}

k = 0
for i in range(ord('A'), ord('Z')+1):
    if chr(i+13) > 'Z':
        ROT13_dict[chr(i)] = chr(ord('A')+ k)
        k += 1
    else:
        ROT13_dict[chr(i)] = chr(i+13)

j = 0
for i in range(ord('a'), ord('z')+1):
    if chr(i+13) > 'z':
        ROT13_dict[chr(i)] = chr(ord('a')+ j)
        j += 1
    else:
        ROT13_dict[chr(i)] = chr(i+13)

for s in string:
    if s.isalpha():
        print(ROT13_dict[s], end='')
    else:
        print(s, end='')
