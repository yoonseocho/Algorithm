from collections import deque

def solution(priorities, location):
    q = deque()
    cnt = 0
    
    for idx, val in enumerate(priorities):
        q.append((idx, val))
    
    while q:
        if q[0][1] == max(q, key=lambda x: x[1])[1]:
            if q[0][0] == location:
                return cnt + 1
            q.popleft()
            cnt += 1
        else:
            q.append(q.popleft())
            
    