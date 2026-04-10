import sys

input = sys.stdin.readline

def is_available(pwd):
    vowels = {"a", "e", "i", "o", "u"}

    for char in pwd:
        if char in vowels:
            break
    else:
        return False
    
    v_cnt, c_cnt = 0, 0

    for i in range(len(pwd)):
        if i>0 and pwd[i] == pwd[i-1]:
            if pwd[i] not in {"e", "o"}:
                return False
        if pwd[i] in vowels:
            v_cnt += 1
            c_cnt = 0
        else:
            v_cnt = 0
            c_cnt += 1
        
        if v_cnt >= 3 or c_cnt >= 3:
            return False
    return True

while True:
    pwd = input().strip()

    if pwd == "end":
        break

    if is_available(pwd):
        print(f"<{pwd}> is acceptable.")
    else:
        print(f"<{pwd}> is not acceptable.")