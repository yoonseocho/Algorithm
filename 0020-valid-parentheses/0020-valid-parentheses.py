class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for char in s:
            if char in "({[":
                stk.append(char)
            else:
                if not stk:
                    return False
                else:
                    if stk[-1] == "(" and char == ")":
                        stk.pop()
                    elif stk[-1] == "{" and char == "}":
                        stk.pop()
                    elif stk[-1] == "[" and char == "]":
                        stk.pop()
                    
                    else:
                        return False
        
        return False if stk else True