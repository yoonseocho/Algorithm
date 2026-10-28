from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    
    cur_max = max(priorities)
    order = 0
    while q:
        idx, num = q.popleft()
        
        if any(num < x[1] for x in q):
            q.append((idx, num))
        else:
            order += 1
            if idx == location:
                return order
    