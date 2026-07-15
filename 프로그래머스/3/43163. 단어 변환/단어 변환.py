from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    
    def is_one_letter_diff(word1, word2):
        diff_cnt = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff_cnt += 1
            if diff_cnt > 1:
                return False
        
        return diff_cnt == 1
            
    def bfs():
        q = deque([(begin, 0)])

        while q:
            curr_word, cnt = q.popleft()
            
            if curr_word == target:
                return cnt

            for i, word in enumerate(words):
                if is_one_letter_diff(curr_word, word) and not visited[i]:
                    q.append((word, cnt+1))
                    visited[i] = True
                
    return bfs()