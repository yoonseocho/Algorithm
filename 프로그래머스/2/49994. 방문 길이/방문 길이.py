def solution(dirs):
    answer = set()
    x, y, nx, ny = 0, 0, 0, 0
    
    def in_range(x, y):
        return -5 <= x<= 5 and -5 <= y <= 5

    for dir in dirs:
        if dir == "U":
            nx = x
            ny = y + 1
        elif dir == "D":
            nx = x
            ny = y - 1
        elif dir == "R":
            nx = x + 1
            ny = y
        elif dir == "L":
            nx = x - 1
            ny = y
        
        if in_range(nx, ny):
            if (nx, ny, x, y) not in answer:
                answer.add((x, y, nx, ny))
            x, y = nx, ny
    
    return len(answer)