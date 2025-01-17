import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
dq = deque()
output = []

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()

    if(cmd == "pop"):
        output.append(str(dq.popleft()) if dq else "-1")
    elif(cmd == "size"):
        output.append(str(len(dq)))
    elif(cmd == "empty"):
        output.append("0" if dq else "1")
    elif(cmd == "front"):
        output.append(str(dq[0]) if dq else "-1")
    elif(cmd == "back"):
        output.append(str(dq[-1]) if dq else "-1")
    else:
        dq.append(int(cmd.split()[1]))

sys.stdout.write("\n".join(output) + '\n')