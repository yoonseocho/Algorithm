memo = {}

def solution(n, words):
    last = words[0][-1]
    memo[words[0]] = 1
    for idx, word in enumerate(words[1:], start=1):
        order = (idx % n) + 1
        turn = idx // n + 1
        if word in memo or len(word) == 1 or last != word[0]:
            return [order, turn]
        memo[word] = order
        last = word[-1]
    return [0, 0]
        