def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    one_cnt, two_cnt, three_cnt = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            one_cnt += 1
        if answers[i] == second[i%len(second)]:
            two_cnt += 1
        if answers[i] == third[i%len(third)]:
            three_cnt += 1
    
    answer = []
    if one_cnt == max(one_cnt, two_cnt, three_cnt):
        answer.append(1)
    if two_cnt == max(one_cnt, two_cnt, three_cnt):
        answer.append(2)
    if three_cnt == max(one_cnt, two_cnt, three_cnt):
        answer.append(3)
    return answer