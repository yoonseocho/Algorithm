from collections import Counter

def solution(k, tangerine):
    c = Counter(tangerine)
    kind, cnt = 0, 0
    for key, value in c.most_common():
        if cnt >= k:
            return kind
        cnt += value
        kind += 1
    return kind