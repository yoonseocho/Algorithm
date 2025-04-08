import sys
from collections import deque

input = sys.stdin.readline

# 동, 남, 서, 북 (시계 방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_score(x, y): # 주사위가 도착한 칸 (x, y)에 대한 점수를 획득
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    num = board[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == num:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1

    return count * num


def roll_dice(direction):
    temp = dice[:]

    top = temp[1]
    north = temp[2]
    east = temp[3]
    west = temp[4]
    south = temp[5]
    bottom = temp[6]

    if direction == 0: # 동
        dice[1] = west
        dice[3] = top
        dice[4] = bottom
        dice[6] = east
    elif direction == 1: # 남
        dice[1] = north
        dice[2] = bottom
        dice[5] = top
        dice[6] = south
    elif direction == 2: # 서
        dice[1] = east
        dice[3] = bottom
        dice[4] = top
        dice[6] = west
    elif direction == 3: # 븍
        dice[1] = south
        dice[2] = top
        dice[5] = bottom
        dice[6] = north


def get_bottom_of_dice():
    return dice[6]

def get_direction_of_dice(a, b, direction): # 주사위 이동 방향
    if a > b: # 90도 시계 방향 회전
        return (direction + 1) % 4
    elif a < b: # 90도 반시계 방향 회전
        return (direction + 3) % 4
    else: # 변화 X 그대로
        return direction

def simulation():
    global dice

    x, y = 0, 0
    direction = 0
    total_score = 0

    for _ in range(k):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if not (0 <= nx < n and 0 <= ny < m):
            direction = (direction + 2) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        roll_dice(direction)

        x = nx
        y = ny

        total_score += get_score(x, y)
        
        a = get_bottom_of_dice()
        b = board[x][y]
        direction = get_direction_of_dice(a, b, direction)

    return total_score


n, m, k = map(int, input().split())
board = []
for _ in range(n):
    line = map(int, input().split())
    row = list(line)
    board.append(row)
dice = [0, 1, 2, 3, 4, 5, 6]

print(simulation())
    