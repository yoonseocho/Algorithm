from collections import deque

def is_right(q):
    stk = []
    
    for each in q:
        if each == "]":
            if stk and stk[-1] == "[":
                stk.pop()
            else:
                return False
        elif each == "}":
            if stk and stk[-1] == "{":
                stk.pop()
            else:
                return False
        elif each == ")":
            if stk and stk[-1] == "(":
                stk.pop()
            else:
                return False
        else:
            stk.append(each)
        #print(stk)
    return False if stk else True

def solution(s):
    q = deque(s)
    cnt = 0

    for _ in range(len(s)):
        q.append(q.popleft())
        if is_right(q):
            cnt += 1
        #print(q, is_right(q))
    return cnt
        