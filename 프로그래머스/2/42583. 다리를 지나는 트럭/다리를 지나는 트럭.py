from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    time = 0
    total_weight = 0
    truck_weights = deque(truck_weights)
    
    while bridge:
        time += 1
        total_weight -= bridge.popleft()
        
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)
    return time