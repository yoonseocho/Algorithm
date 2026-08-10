def solution(people, limit):
    n = len(people)
    people.sort(reverse=True)
    cnt = 0
    
    l, r = 0, n-1
    
    while l<=r:
        if people[l] + people[r] > limit:
            l += 1
        else:
            l += 1
            r -= 1
        cnt += 1
    return cnt
    
    