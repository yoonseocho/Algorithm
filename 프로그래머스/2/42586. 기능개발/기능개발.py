import math

def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        days.append(day)

    stk = []
    ans = []
    for day in days:
        cnt = 0
        while stk and stk[0] < day:
            stk.pop()
            cnt += 1
        if cnt != 0:
            ans.append(cnt)
        stk.append(day)
    
    cnt = 0
    while stk:
        stk.pop()
        cnt += 1
    ans.append(cnt)
    
    return ans