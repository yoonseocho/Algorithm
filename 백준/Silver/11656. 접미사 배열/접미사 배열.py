S = input()
output = []
for i in range(len(S)):
    output.append(S[i:])
output.sort()
print('\n'.join(output))