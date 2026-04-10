import sys

def Solution():
    S = sys.stdin.readline().strip()
    i = 0
    while i < len(S):
        if S[i:i+2] == "pi" or S[i:i+2] == "ka":
            i += 2
        elif S[i:i+3] == "chu":
            i += 3
        else:
            print("NO")
            return
    print("YES")

Solution()