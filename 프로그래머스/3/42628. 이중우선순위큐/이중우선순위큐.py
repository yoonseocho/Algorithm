def solution(operations):
    q = []
    
    for operation in operations:
        cmd, data = operation.split()
        if cmd == "I":
            q.append(int(data))
        elif q and data == "1":
            q.sort()
            q.pop()
        elif q and data == "-1":
            q.sort(reverse=True)
            q.pop()

    return [max(q), min(q)] if q else [0, 0]