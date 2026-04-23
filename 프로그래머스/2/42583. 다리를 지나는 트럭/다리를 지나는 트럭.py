from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([each for each in truck_weights])
    on_bridges = deque()
    
    time = 0
    while True:
        if not q and not on_bridges:
            break
        time += 1
        
        # 다리 위 탈출 조건
        if on_bridges and on_bridges[0][1] == bridge_length:
            on_bridges.popleft()
        
        # 다리 위에 올라갈 조건
        if q and q[0] + sum(weight for weight, _ in on_bridges) <= weight and len(on_bridges) + 1 <= bridge_length:
            curr = q.popleft()
            on_bridges.append([curr, 0])
            
        for on_bridge in on_bridges:
            on_bridge[1] += 1
        
        # print(time, q, on_bridges)
        
            
        
    return time
        