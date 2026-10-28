def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        day = -((p - 100) // s)
        days.append(day)

    ans = []
    
    current = days[0]
    cnt = 1
    
    for i in range(1, len(days)):
        if current >= days[i]:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            current = days[i]
    ans.append(cnt)
    return ans