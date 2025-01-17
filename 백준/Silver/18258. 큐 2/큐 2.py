# 10845와 똑같지만 '시간초과'를 해결하는 법: pop에서 deque을 쓰자

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
que = deque([])

for _ in range(N):
    cmd = input().rstrip()

    if "push" in cmd:
        que.append(int(cmd.split(" ")[1]))

    elif cmd == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif cmd == "size":
        print(len(que))

    elif cmd == "empty":
        if que:
            print(0)
        else:
            print(1)

    elif cmd == "front":
        if que:
            print(que[0])
        else:
            print(-1)

    elif cmd == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
