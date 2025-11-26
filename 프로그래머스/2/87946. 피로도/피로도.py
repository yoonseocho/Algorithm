from itertools import permutations

def solution(k, dungeons):
    p_list = list(permutations(dungeons, len(dungeons)))
    cnt = [0] * len(p_list)
    
    for i in range(len(p_list)):
        tmp_k = k
        for min_p, exhausted in p_list[i]:
            if tmp_k < min_p:
                continue
            tmp_k -= exhausted
            cnt[i] += 1
    
    return max(cnt)