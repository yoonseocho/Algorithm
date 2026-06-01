from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time = 0
    
    while truck_weights:
        q.pop()
        time += 1
        if sum(q) + truck_weights[0] <= weight:
            q.appendleft(truck_weights.popleft())
        else:
            q.appendleft(0)
        # print(q)
    
    return time + bridge_length