def is_same(memo, want, number):
    for key, value in zip(want, number):
        if key not in memo or memo[key] != value:
            return False
    return True

def solution(want, number, discount):
    possible = 0
    for i in range(len(discount)-9):
        memo = {}
        for j in range(i, i+10):
            if discount[j] not in memo:
                memo[discount[j]] = 1
                continue
            memo[discount[j]] += 1
        if is_same(memo, want, number):
            possible += 1
    return possible