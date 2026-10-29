class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for p in s:
            if not stk and (p == ")" or p == "}" or p == "]"):
                return False
            
            if stk:
                if stk[-1] == "(" and p == ")":
                    stk.pop()
                    continue
                elif stk[-1] == "{" and p == "}":
                    stk.pop()
                    continue
                elif stk[-1] == "[" and p == "]":
                    stk.pop()
                    continue
            
            if p in "({[":
                stk.append(p)
            else:
                return False

        return False if stk else True