def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses, speeds):
        day = -((progress-100)//speed)
        days.append(day)
    
    release = []
    max_num = 0
    for day in days:
        if day > max_num:
            max_num = day
            release.append(1)
        else:   
            release[-1] += 1
    
    return release