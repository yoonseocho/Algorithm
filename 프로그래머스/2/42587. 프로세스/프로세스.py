from collections import deque

def solution(priorities, location):
    q = deque()
    
    for idx, p in enumerate(priorities):
        q.append((idx, p))
    
    priorities.sort(reverse=True)
    
    answer = 0
    while q:
        each = q.popleft()
        if each[1] < priorities[answer]:
            q.append(each)
        else:
            answer += 1
            if location == each[0]:
                return answer