from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]) * bridge_length
    q = deque(truck_weights)
    
    time = 0
    current_sum = 0
    
    while q or current_sum > 0:
        # 차 내보내기
        car_out = bridge.popleft()
        current_sum -= car_out
        
        # 차 들이기
        if q and current_sum + q[0] <= weight:
            car_in = q.popleft()
            bridge.append(car_in)
            current_sum += car_in
        else:
            bridge.append(0)
        
        time += 1
    
    return time