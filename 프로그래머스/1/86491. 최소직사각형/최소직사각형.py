def solution(sizes):
    max_w, max_h = 0, 0
    
    for w, h in sizes:
        big, small = max(w, h), min(w, h)
        
        max_w = max(max_w, big)
        max_h = max(max_h, small)
    
    return max_w * max_h