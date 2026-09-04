def solution(s):
    s = s[2:-2].split('},{')
    
    new_s = [list(map(int, each.split(','))) for each in s]
    
    new_s.sort(key=lambda x: len(x))
    
    answer = []
    for nums in new_s:
        for num in nums:
            if num in answer:
                continue
            answer.append(num)
    return answer