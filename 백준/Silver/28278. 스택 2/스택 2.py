import sys

input = sys.stdin.readline
stk = []
output = []

for _ in range(int(input().rstrip())):
    cmd = input().rstrip().split()
    if(cmd[0] == "1"):
        stk.append(int(cmd[1]))
    elif(cmd[0] == "2"):
        output.append(stk.pop() if stk else -1)
    elif(cmd[0] == "3"):
        output.append(len(stk))
    elif(cmd[0] == "4"):
        output.append(1 if len(stk) == 0 else 0)
    elif(cmd[0] == "5"):
        output.append(stk[-1] if stk else -1)

sys.stdout.write("\n".join(map(str, output)) + '\n')
                   