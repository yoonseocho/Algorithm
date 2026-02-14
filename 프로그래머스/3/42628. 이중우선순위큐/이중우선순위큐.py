from heapq import heapify, heappop

def solution(operations):
    q = []
    
    for operation in operations:
        cmd, data = operation.split()
        if cmd == "I":
            q.append(int(data))
        elif q and data == "1":
            q.remove(max(q))
        elif q and data == "-1":
            heapify(q)
            heappop(q)
    
    return [max(q), min(q)] if q else [0,0]