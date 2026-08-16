def solution(s):
    
    def is_valid(s):
        stk = []
        
        for chr in s:
            if not stk and (chr == "]" or chr == ")" or chr == "}"):
                return False
            
            if chr == "]":
                if stk and stk[-1] == "[":
                    stk.pop()
                    continue
                else:
                    return False
            
            elif chr == ")":
                if stk and stk[-1] == "(":
                    stk.pop()
                    continue
                else:
                    return False
            
            elif chr == "}":
                if stk and stk[-1] == "{":
                    stk.pop()
                    continue
                else:
                    return False
            
            stk.append(chr)
        
        return False if stk else True
    
    cnt = 0
    for x in range(len(s)):
        rotated_s = s[x:] + s[:x]
        if is_valid(rotated_s):
            cnt += 1
    return cnt
            