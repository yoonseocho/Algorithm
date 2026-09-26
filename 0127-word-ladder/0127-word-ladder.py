from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        # 와일드카드 만들기
        m = len(wordList[0])
        pattern_dict = defaultdict(list)
        for word in wordList:
            for i in range(m):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_dict[pattern].append(word)
        
        # bfs
        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            curr_word, cnt = q.popleft()

            if curr_word == endWord:
                return cnt

            for i in range(m):
                pattern = curr_word[:i] + "*" + curr_word[i+1:]
                for next_word in pattern_dict[pattern]:
                    if next_word not in visited:
                        q.append((next_word, cnt + 1))
                        visited.add(next_word)
        
        return 0