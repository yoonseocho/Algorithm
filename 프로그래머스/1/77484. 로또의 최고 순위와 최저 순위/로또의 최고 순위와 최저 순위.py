from collections import Counter

def solution(lottos, win_nums):
    prize_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    lottos_dict = Counter(lottos)
    
    answer = 0
    for num in win_nums:
        if num in lottos_dict and lottos_dict[num] != 0:
            answer += 1
            lottos_dict[num] -= 1
    
    return [prize_dict[answer+lottos_dict[0]], prize_dict[answer]]