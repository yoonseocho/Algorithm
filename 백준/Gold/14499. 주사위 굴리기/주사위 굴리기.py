import sys

input = sys.stdin.readline

# 동 서 북 남
dx = [0, 0, -1, 1] 
dy = [1, -1, 0, 0]

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
        dice[1] = east
        dice[3] = bottom
        dice[4] = top
        dice[6] = west
    elif direction == 3:
        dice[1] = south
        dice[2] = top
        dice[5] = bottom
        dice[6] = north
    elif direction == 4:
        dice[1] = north
        dice[2] = bottom
        dice[5] = top
        dice[6] = south


def solution():
    global x, y
    for i in range(k):
        direction = command[i]
        nx = x + dx[direction-1]
        ny = y + dy[direction-1]

        if not(0 <= nx < n and 0 <= ny < m):
            continue

        roll_dice(direction)
        
        x = nx
        y = ny
        if board[x][y] == 0:
            board[x][y] = dice[6]
        else:
            dice[6] = board[x][y]
            board[x][y] = 0

        print(dice[1])

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0] * 7

solution()