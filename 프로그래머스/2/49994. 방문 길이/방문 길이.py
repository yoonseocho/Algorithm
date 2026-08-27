def solution(dirs):
    answer = set()
    x, y = 0, 0
    d = {"U":(0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0)}
    
    def in_range(x, y):
        return -5 <= x<= 5 and -5 <= y <= 5

    for dir in dirs:
        nx, ny = x + d[dir][0], y + d[dir][1]
        
        if in_range(nx, ny):
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x, y = nx, ny
    
    return len(answer)//2