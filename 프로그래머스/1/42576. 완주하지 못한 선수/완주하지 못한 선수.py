from collections import Counter

def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    
    answer = a-b
    return list(answer.keys())[0]