from collections import deque

def remove_max(q):
    if not q:
        return
    
    max_val = float('-inf')
    for element in q:
        max_val = max(element, max_val)

    while True:
        if q[0] == max_val:
            q.popleft()
            break
        else:
            q.append(q.popleft())

def remove_min(q):
    if not q:
        return
    
    min_val = float('inf')
    for element in q:
        min_val = min(element, min_val)

    while True:
        if q[0] == min_val:
            q.popleft()
            break
        else:
            q.append(q.popleft())

def solution(operations):
    q = deque()
    
    for operation in operations:
        cmd, data = operation.split()
        if cmd == "I":
            q.append(int(data))
        elif cmd == "D" and data == "1":
            remove_max(q)
        elif cmd == "D" and data == "-1":
            remove_min(q)

    return [max(q), min(q)] if q else [0, 0]