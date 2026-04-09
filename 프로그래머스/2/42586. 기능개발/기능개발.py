import math

def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100-progress) / speed)
        days.append(day)
    # 7 3 9 -> 2 1
    current = days[0]
    cnt = 1
    ans = []
    for i in range(1, len(days)):
        if current >= days[i]:
            cnt += 1
        else:
            ans.append(cnt)
            current = days[i]
            cnt = 1
    ans.append(cnt)
    return ans
        
        
            