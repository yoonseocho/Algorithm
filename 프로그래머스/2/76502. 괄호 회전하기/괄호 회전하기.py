def solution(s):
    
    def is_valid(s):
        stk = []
        pairs = {")":"(", "}":"{", "]":"["}
        
        for chr in s:
            if chr in pairs:
                if not stk or stk[-1] != pairs[chr]:
                    return False
                stk.pop()
            
            else:
                stk.append(chr)
        
        return not stk
    
    cnt = 0
    for x in range(len(s)):
        rotated_s = s[x:] + s[:x]
        if is_valid(rotated_s):
            cnt += 1
    return cnt
            