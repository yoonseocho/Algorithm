from collections import deque

def load_new_truck(on_bridge, q):
    truck_weight, each_time = q.popleft()
    each_time += 1
    on_bridge.append([truck_weight, each_time])
    
def handle_exist_truck(on_bridge):
    for each_truck in on_bridge:
        each_truck[1] += 1

def can_go(on_bridge, q, weight, bridge_length):
    total_weight = sum(each_truck[0] for each_truck in on_bridge)
    return total_weight + q[0][0] <= weight and len(on_bridge) + 1 <= bridge_length


def can_finish_bridge(on_bridge, bridge_length):
    return on_bridge[0][1] == bridge_length

def init(truck_weights):
    q = deque()
    for truck_weight in truck_weights:
        q.append([truck_weight, 0])
    
    time = 0
    on_bridge = deque()
    off_bridge = deque()
    
    load_new_truck(on_bridge, q)
    time += 1
    
    return q, on_bridge, off_bridge, time
    
def solution(bridge_length, weight, truck_weights):
    
    q, on_bridge, off_bridge, time = init(truck_weights)
    
    while on_bridge:
        # 1. 다리 탈출
        if can_finish_bridge(on_bridge, bridge_length):
            truck = on_bridge.popleft()
            off_bridge.append(truck)
        
        if q:
            # 2. 다리 위에 못 올라감
            if not can_go(on_bridge, q, weight, bridge_length):
                handle_exist_truck(on_bridge)
                time += 1
                continue

            # 3. 다리 위에 올라감
            # 3-1. 기존 다리 위에 있는 시간 더해주고
            handle_exist_truck(on_bridge)
            # 3-2. 새로운 트럭 투입
            load_new_truck(on_bridge, q)
            time += 1
        else:
            handle_exist_truck(on_bridge)
            time += 1
        
    return time
        