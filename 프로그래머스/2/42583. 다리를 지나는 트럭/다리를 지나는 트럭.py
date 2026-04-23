from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    curr_weight = 0
    time = 0 
    
    while bridge:
        time += 1
        curr_weight -= bridge.popleft()
        
        # 다리에 들어가는 조건
        if q:
            if q[0] + curr_weight <= weight:
                curr = q.popleft()
                bridge.append(curr)
                curr_weight += curr
            else:
                bridge.append(0)
            
    
        #print(time, q, bridge)
    
    return time
        