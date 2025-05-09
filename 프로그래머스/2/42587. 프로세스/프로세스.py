from collections import deque

def solution(priorities, location):
    q = deque((idx, p) for idx, p in enumerate(priorities))
    count = 0
    
    while q:
        idx, p = q.popleft()
        
        if p == max(priorities):
            count += 1
            priorities.remove(p)
            if idx == location:
                return count
        else:
            q.append((idx,p))
            