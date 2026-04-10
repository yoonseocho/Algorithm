import sys

input = sys.stdin.readline

S = list(input().strip())

zero_cnt = S.count('0') // 2
one_cnt = S.count("1") // 2

# 앞에서부터 1 제거
cnt = 0
for i in range(len(S)):
    if S[i] == '1':
        S[i] = ''
        cnt += 1
    if cnt == one_cnt:
        break

# 뒤에서부터 0 제거
cnt = 0
for i in range(len(S)-1, -1, -1):
    if S[i] == '0':
        S[i] = ''
        cnt += 1
    if cnt == zero_cnt:
        break

print(''.join(S))
