from collections import deque
import sys

dq = deque()
output = []

for _ in range(int(sys.stdin.readline().rstrip())):
    cmd = sys.stdin.readline().rstrip()
    if(cmd == "3"):
        output.append(dq.popleft() if dq else -1)
    elif(cmd == "4"):
        output.append(dq.pop() if dq else -1)
    elif(cmd == "5"):
        output.append(len(dq))
    elif(cmd == "6"):
        output.append(1 if len(dq) == 0 else 0)
    elif(cmd == "7"):
        output.append(dq[0] if dq else -1)
    elif(cmd == "8"):
        output.append(dq[-1] if dq else -1)
    else:
        if(cmd.split()[0] == "1"):
            dq.appendleft(int(cmd.split()[1]))
        elif(cmd.split()[0] == "2"):
            dq.append(int(cmd.split()[1]))
    
sys.stdout.write("\n".join(map(str, output))+"\n")