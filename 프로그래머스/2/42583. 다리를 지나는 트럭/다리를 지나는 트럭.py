from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    current_weight = 0
    
    while bridge:
        time += 1
        # 1. 다리에서 트럭 (혹은 빈 공간 0)이 나감
        exited = bridge.popleft()
        current_weight -= exited
        
        # 2. 다음 트럭이 다리에 올라올 수 있는지 확인
        if truck_weights:
            if truck_weights[0] + current_weight <= weight:
                new_truck = truck_weights.popleft()
                bridge.append(new_truck)
                current_weight += new_truck
            else:
                bridge.append(0)
    
    return time
    