def solution(brown, yellow):
    for h in range(3, brown):
        for w in range(h, brown):
            if 2*w + 2*h - 4 == brown and (w-2)*(h-2) == yellow:
                return [w, h]