def solution(s):
    val = list(map(int, s.split()))
    
    min_val = min(val)
    max_val = max(val)
    
    return f"{min_val} {max_val}"