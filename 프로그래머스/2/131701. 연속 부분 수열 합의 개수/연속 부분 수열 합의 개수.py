from collections import deque

def solution(elements):
    q = deque(elements)
    memo = set()
    
    for _ in range(len(q)):
        start = 0
        rear = len(q)-1
        tmp_sum = sum(q)
        memo.add(tmp_sum)
        while start != rear:
            tmp_sum -= q[rear]
            rear -= 1
            if tmp_sum not in memo:
                memo.add(tmp_sum)
        curr_element = q.popleft()
        q.append(curr_element)
    return len(memo)