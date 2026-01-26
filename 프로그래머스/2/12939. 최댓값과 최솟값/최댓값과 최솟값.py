def solution(s):
    val = list(map(int, s.split()))
    return f"{min(val)} {max(val)}"