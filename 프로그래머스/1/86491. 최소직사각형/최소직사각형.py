def solution(sizes):
    new_sizes = []
    for size in sizes:
        new_sizes.append(sorted(size))
        
    ws = []
    hs = []
    for w, h in new_sizes:
        ws.append(w)
        hs.append(h)
    
    return max(ws) * max(hs)