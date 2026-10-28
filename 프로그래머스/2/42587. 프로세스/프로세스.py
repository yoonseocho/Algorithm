from collections import deque

def solution(priorities, location):
    q = deque()
    for i, p in enumerate(priorities):
        q.append((p, i))
    
    cur_max = max(priorities)
    order = 0
    while q:
        num, idx = q.popleft()
        
        if not q:
            order += 1
            if idx == location:
                return order
            
        cur_max = max(q, key=lambda x: x[0])[0]
        
        if num < cur_max:
            q.append((num, idx))
        else:
            order += 1
            if idx == location:
                return order
    