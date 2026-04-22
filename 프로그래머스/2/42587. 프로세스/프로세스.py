from collections import deque

def solution(priorities, location):
    q = deque()
    
    for idx, p in enumerate(priorities):
        q.append((idx, p))
    
    max_num = max(priorities)
    result = []
    while q:
        each = q.popleft()
        if each[1] < max_num:
            q.append(each)
        else:
            result.append(each)
            if q:
                max_num = max(q, key = lambda x: x[1])[1]
    for i, (idx, _) in enumerate(result):
        if idx == location:
            return i + 1