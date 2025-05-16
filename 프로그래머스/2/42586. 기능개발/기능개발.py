import math

def solution(progresses, speeds):
    days = []
    stk = []
    answer = []
    
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)

    for day in days:
        if not stk or (stk and stk[0] >= day):
            stk.append(day)
        elif stk and stk[0] < day:
            cnt = 0
            while stk and stk[0] < day:
                stk.pop()
                cnt += 1
            answer.append(cnt)
            stk.append(day)
 
    if stk:
        answer.append(len(stk))
    return answer