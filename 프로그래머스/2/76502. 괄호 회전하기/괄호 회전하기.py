def is_right(rotated):
    stk = []
    pairs = {")":"(", "}":"{", "]":"["}
    
    for char in rotated:
        if char in pairs:
            if not stk or stk.pop() != pairs[char]:
                return False
        else:
            stk.append(char)

    return not stk
                

def solution(s):
    if len(s) % 2 != 0:
        return 0
    
    cnt = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        #print(rotated, is_right(rotated))
        if is_right(rotated):
            cnt += 1
    return cnt
        