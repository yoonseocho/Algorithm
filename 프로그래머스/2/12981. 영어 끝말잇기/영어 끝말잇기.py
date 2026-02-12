def solution(n, words):
    memo = set()
    prev_word = words[0][0]
    for idx, word in enumerate(words):
        order = (idx % n) + 1
        turn = idx // n + 1
        if word in memo or prev_word != word[0]:
            return [order, turn]
        memo.add(word)
        prev_word = word[-1]
    return [0, 0]
        