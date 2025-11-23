def solution(sizes):
    long_sides = []
    short_sides = []
    
    for size in sizes:
        big = max(size)
        short = min(size)
        
        long_sides.append(big)
        short_sides.append(short)
    
    return max(long_sides) * max(short_sides)
    
    