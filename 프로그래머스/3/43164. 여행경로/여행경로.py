def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    n = len(tickets)
    visited = [False] * n
    path = ["ICN"]
    def dfs(curr_city, path):
        if len(path) == n+1:
            return True
        
        for idx, (start, dest) in enumerate(tickets):
            if not visited[idx] and curr_city == start:
                visited[idx] = True
                path.append(dest)
                
                if dfs(dest, path):
                    return True
                
                path.pop()
                visited[idx] = False
    
    if dfs("ICN", path):
        return path
            