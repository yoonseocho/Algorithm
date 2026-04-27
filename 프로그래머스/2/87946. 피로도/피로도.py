from itertools import permutations

def solution(k, dungeons):
    cases = permutations(dungeons, len(dungeons))
    max_cnt = 0
    for case in cases:
        cnt = 0
        curr_energy = k
        for min_need, cost in case:
            if curr_energy >= min_need:
                curr_energy -= cost
                cnt += 1
        max_cnt = max(max_cnt, cnt)
        if cnt == len(dungeons):
            return cnt
    
    return max_cnt
    