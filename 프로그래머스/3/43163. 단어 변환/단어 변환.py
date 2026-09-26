from collections import deque

def solution(begin, target, words):
    n = len(words)
    visited = [0] * n
    
    def is_one_letter_diff(word1, word2):
        diff = 0
        for ch1, ch2 in zip(word1, word2):
            if ch1 != ch2:
                diff += 1
        
        return True if diff == 1 else False
    
    # bfs
    def bfs(word, cnt):
        q = deque([(word, cnt)])
        
        while q:
            curr_word, cnt = q.popleft()
            
            if curr_word == target:
                return cnt
            
            for i, word in enumerate(words):
                if not visited[i] and is_one_letter_diff(curr_word, word):
                    q.append((word, cnt + 1))
                    visited[i] = cnt + 1
        
        return 0
    
    return bfs(begin, 0)