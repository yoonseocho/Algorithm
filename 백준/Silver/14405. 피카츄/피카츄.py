import sys

def Solution():
    S = sys.stdin.readline().strip()
    S = S.replace("pi", " ").replace("ka", " ").replace("chu", " ")

    if S.strip() == "":
        print("YES")
    else:
        print("NO")
Solution()