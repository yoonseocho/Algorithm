def solution(people, limit):
    people.sort()
    n = len(people)
    start, end = 0, n-1
    cnt = 0
    while start <= end:
        if people[start] + people[end] > limit:
            end -= 1
            cnt += 1
            continue
        cnt += 1
        start += 1
        end -= 1
    return cnt
        
        