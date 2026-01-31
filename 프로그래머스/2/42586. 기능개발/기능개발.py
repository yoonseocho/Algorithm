import math

def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100-progress)/speed)
        days.append(day)
    
    answer = []
    max_num = -1
    cnt = 0
    for day in days:
        if day > max_num:
            max_num = day
            if cnt != 0:
                answer.append(cnt)
            cnt = 1
        else:   
            cnt += 1
    answer.append(cnt)
    return answer