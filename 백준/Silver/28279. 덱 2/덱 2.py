from collections import deque
import sys

dq = deque()
output = []

input = sys.stdin.readline

for _ in range(int(input().strip())):
    cmd = input().strip().split()
    if(cmd[0] == "1"):
        dq.appendleft(int(cmd[1]))
    elif(cmd[0] == "2"):
        dq.append(int(cmd[1]))
    elif(cmd[0] == "3"):
        output.append(dq.popleft() if dq else -1)
    elif(cmd[0] == "4"):
        output.append(dq.pop() if dq else -1)
    elif(cmd[0] == "5"):
        output.append(len(dq))
    elif(cmd[0] == "6"):
        output.append(1 if len(dq) == 0 else 0)
    elif(cmd[0] == "7"):
        output.append(dq[0] if dq else -1)
    elif(cmd[0] == "8"):
        output.append(dq[-1] if dq else -1)

sys.stdout.write("\n".join(map(str, output))+"\n")