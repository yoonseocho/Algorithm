from collections import deque

def solution(priorities, location):
    q = deque()
    
    for idx, priority in enumerate(priorities):
        q.append((idx, priority))
        
    priorities.sort(reverse=True)
    
    cnt = 0
    while q:
        idx, priority = q.popleft()
        if priority == priorities[cnt]:
            cnt += 1
            if idx == location:
                return cnt
        else:
            q.append((idx, priority))
        