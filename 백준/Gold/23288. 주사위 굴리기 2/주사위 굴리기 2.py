import sys
from collections import deque

input = sys.stdin.readline

# 시계 방향 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def roll_dice(direction):
    global dice

    top = dice[1]
    north = dice[2]
    east = dice[3]
    west = dice[4]
    south = dice[5]
    bottom = dice[6]

    if direction == 1:
        dice[1] = west
        dice[3] = top
        dice[4] = bottom
        dice[6] = east
    elif direction == 2:
        dice[1] = north
        dice[2] = bottom
        dice[5] = top
        dice[6] = south
    elif direction == 3:
        dice[1] = east
        dice[3] = bottom
        dice[4] = top
        dice[6] = west
    elif direction == 4:
        dice[1] = south
        dice[2] = top
        dice[5] = bottom
        dice[6] = north

def get_score(x, y):
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    num = board[x][y]
    count = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (0 <= nx < n and 0 <= ny < m) and not visited[nx][ny] and board[nx][ny] == num:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
    return count * num

def solution():
    global x, y

    direction = 0
    total_score = 0

    for i in range(k):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if not (0<= nx < n and 0<= ny < m):
            direction = (direction + 2) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        x = nx
        y = ny

        roll_dice(direction+1)

        total_score += get_score(x, y)

        A = dice[6]
        B = board[x][y]
        if A > B:
            direction = (direction + 1) % 4
        elif A < B:
            direction = (direction + 3) % 4

    return total_score



n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
x = y = 0
dice = [0, 1, 2, 3, 4, 5, 6]

print(solution())