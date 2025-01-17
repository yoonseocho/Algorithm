import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
deque = deque()

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()

    if(cmd == "pop"):
        if(deque):
            print(deque.popleft())
        else:
            print(-1)
    elif(cmd == "size"):
        print(len(deque))
    elif(cmd == "empty"):
        if(deque):
            print(0)
        else:
            print(1)
    elif(cmd == "front"):
        if(deque):
            print(deque[0])
        else:
            print(-1)
    elif(cmd == "back"):
        if(deque):
            print(deque[-1])
        else:
            print(-1)
    else:
        cmd, val = cmd.split()
        val = int(val)
        deque.append(val)