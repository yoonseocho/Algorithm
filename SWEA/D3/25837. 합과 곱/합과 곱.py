import math

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s, p = map(int, input().split())
    d = s**2 - 4*p
    
    if d >= 0:
        root_d = int(math.sqrt(d))
        if root_d * root_d == d:
            if (s+root_d) % 2 == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")