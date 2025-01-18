class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            elif stack and stack[-1] == i:
                    stack.pop()
            else:
                return False
        return not stack