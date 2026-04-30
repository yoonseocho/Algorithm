def solution(tickets):
    n = len(tickets)
    visited = [False] * n
    results = []
    path = ["ICN"]
    indent = "  "
    def dfs(path, cnt, next_start):
        nonlocal results
        #print(indent*cnt + f"ENTER: path={path}, cnt={cnt}, next_start={next_start}")
        if cnt == n:
            results.append(path[:])
            #print(indent*cnt + f"END: path={path}, cnt={cnt}, results={results}")
            return
        
        for idx, (start, dest) in enumerate(tickets):
            if not visited[idx] and next_start == start:
                visited[idx] = True
                path.append(dest)
                #print(indent*cnt + f"BEFORE DFS: path={path}, cnt={cnt}, visited={visited}")
                dfs(path, cnt+1, dest)
                
                path.pop()
                visited[idx] = False
                #print(indent*cnt + f"AFTER DFS: path={path}, cnt={cnt}, visited={visited}")
    
    dfs(path, 0, "ICN")
    
    results.sort()
    #print(results)
    return results[0]
            