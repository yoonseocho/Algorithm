def solution(sizes):
    long_sides = []
    short_sides = []
    
    for size in sizes:
        long_sides.append(max(size))
        short_sides.append(min(size))
    
    return max(long_sides)*max(short_sides)
        