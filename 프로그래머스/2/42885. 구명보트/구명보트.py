def solution(people, limit):
    people.sort()
    start, end = 0, len(people)-1
    cnt = 0
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            cnt += 1
        end -= 1
    return len(people) - cnt
        
        