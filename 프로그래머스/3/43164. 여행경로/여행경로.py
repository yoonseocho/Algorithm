def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    path = ["ICN"]
    n = len(tickets)+1
    visited = [False] * len(tickets)
    
    def dfs(start, path):
        if len(path) == n:
            return True
        
        for i, (s, e) in enumerate(tickets):
            if not visited[i] and s == start:
                visited[i] = True
                path.append(e)
                if dfs(e, path):
                    return True
                path.pop()
                visited[i] = False
    
    dfs("ICN", path)
    return path