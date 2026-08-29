class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        cur_str = ""
        cur_num = 0

        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == "[":
                stk.append((cur_str, cur_num))
                cur_str, cur_num = "", 0
            elif ch == "]":
                prev_str, num = stk.pop()
                cur_str = prev_str + cur_str * num
            else:
                cur_str += ch
        return cur_str