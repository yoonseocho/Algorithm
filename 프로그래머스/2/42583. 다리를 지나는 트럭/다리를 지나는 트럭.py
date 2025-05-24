from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()
    
    for truck in truck_weights:
        q.append([truck, 0])
    
    bridge = deque([[q[0][0], q[0][1] + 1]])
    q.popleft()
    
    time = 1
    
    while bridge:
        
        if bridge and bridge[0][1] == bridge_length:
                bridge.popleft()
        
        if q and sum(truck[0] for truck in bridge) + q[0][0] <= weight:
            bridge.append(q.popleft())
        
        time += 1
        for i in range(len(bridge)):
            bridge[i][1] += 1
            
    return time