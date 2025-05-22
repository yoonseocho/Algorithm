from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()
    
    q = deque()
    for val in truck_weights:
        q.append([val, 0])
    bridge.append(q.popleft())
    while bridge:
        time += 1
        if bridge and bridge[0][1] >= bridge_length:
            bridge.popleft()
            
        if q and len(bridge) < bridge_length and sum(x[0] for x in bridge) + q[0][0] <= weight:
            bridge.append(q.popleft())
        
        for t in bridge:
            t[1] += 1

    return time
        