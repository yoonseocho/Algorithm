T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = input()
    left = 0
    right = len(s)-1
    cnt = 0
    flag = False
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if s[left] != 'x' and s[right] != 'x':
                flag = True
                break
            else:
                if s[left] == 'x':
                    left += 1
                else:
                    right -= 1
                cnt += 1
    if flag:
        print(-1)
    else:
        print(cnt)