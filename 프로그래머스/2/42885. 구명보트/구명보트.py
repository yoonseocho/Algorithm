from collections import deque

def solution(people, limit):
    n = len(people)
    people.sort()
    l, r = 0, n-1
    answer = 0
    
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        
        r -= 1
        answer += 1
    
    return answer