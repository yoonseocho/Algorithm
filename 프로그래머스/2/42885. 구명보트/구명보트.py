def solution(people, limit):
    people.sort()
    
    n = len(people)
    l, r = 0, n-1
    cnt = 0
    
    while l <= r:
        summ = people[l] + people[r]
        if summ > limit:
            r -= 1
        else:
            l += 1
            r -= 1
        cnt += 1
    return cnt