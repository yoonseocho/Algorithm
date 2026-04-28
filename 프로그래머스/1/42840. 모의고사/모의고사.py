def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    for i, answer in enumerate(answers):
        if answer == first[i%len(first)]:
            score[0] += 1
        if answer == second[i%len(second)]:
            score[1] += 1
        if answer == third[i%len(third)]:
            score[2] += 1
    
    answer = []
    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx+1)
    return answer