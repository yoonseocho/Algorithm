def solution(n,a,b):
    round = 1
    
    while a*b != 2:
        if (a < b and a % 2 != 0 and b % 2 == 0 and abs(a-b) == 1) or (a > b and b % 2 != 0 and a % 2 == 0 and abs(a-b) == 1):
            break
        a = -((-a)//2)
        b = -((-b)//2)
        round += 1
    return round