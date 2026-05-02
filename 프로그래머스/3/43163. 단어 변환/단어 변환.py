from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    visited = [False] * len(words)
    
    def is_one_letter_diff(word1, word2):
        cnt = 0
        
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                cnt += 1
        return True if cnt == 1 else False
    
    
    def bfs(word, cnt):
        q.append((word, cnt))
        
        while q:
            word, cnt = q.popleft()
            
            if word == target:
                return cnt
            
            for idx, next_word in enumerate(words):
                if is_one_letter_diff(word, next_word) and not visited[idx]:
                    visited[idx] = True
                    q.append((next_word, cnt+1))
    
    return bfs(begin, 0)
    
    
    