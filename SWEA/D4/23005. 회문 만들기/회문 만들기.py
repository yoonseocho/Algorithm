T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = input()
    left = 0
    right = len(s)-1
    cnt = 0
    possible = True
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif s[left] == 'x':
            left += 1
            cnt += 1
        elif s[right] == 'x':
            right -= 1
            cnt += 1
        else:
            possible = False
            break
    
    print(cnt if possible else -1)