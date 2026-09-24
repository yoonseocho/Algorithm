def solution(book_time):
    in_out = []
    
    for s, e in book_time:
        h, m = map(int, s.split(":"))
        H, M = map(int, e.split(":"))
        
        start = h * 60 + m
        end = H * 60 + M + 10
        in_out.append((start, +1))
        in_out.append((end, -1))
    
    in_out.sort()
    
    answer = 0
    cur = 0
    for _, cnt in in_out:
        cur += cnt
        answer = max(answer, cur)
    
    return answer
    
    
    