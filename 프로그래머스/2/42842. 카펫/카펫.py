def solution(brown, yellow):
    total = brown + yellow
    candidates = []
    for h in range(3, brown//2):
        for w in range(3, brown//2):
            if (h-2)*(w-2) == yellow:
                candidates.append((h, w))
    
    for h, w in candidates:
        if h*w - (h-2)*(w-2) == brown:
            return [w, h]