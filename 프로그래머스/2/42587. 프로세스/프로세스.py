from collections import deque

def solution(priorities, location):
    q = deque()
    
    for idx, priority in enumerate(priorities):
        q.append((idx, priority))
    
    cnt = 0
    while q:
        #print(f"{q[0][1]}, {max(q, key=lambda x: x[1])[1]}")
        if q[0][1] == max(q, key=lambda x: x[1])[1]:
            cnt += 1
            if q[0][0] == location:
                break
            q.popleft()
            continue
        q.append(q.popleft())
        #print(q)
    return cnt
        