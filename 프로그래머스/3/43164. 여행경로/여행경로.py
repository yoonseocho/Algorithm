def solution(tickets):
    answers = []
    route = ["ICN"]
    n = len(tickets)
    visited = [False] * n
    indent = "  "
    
    def dfs(start, cnt):
        #print(f"{indent*cnt}>>>dfs({start}, {cnt}) 시작, {route}")
        if cnt == n:
            answers.append(route[:])
            return
        
        for i in range(n):
            if not visited[i] and tickets[i][0] == start:
                route.append(tickets[i][1])
                visited[i] = True
                dfs(tickets[i][1], cnt+1)
                #print(f"{indent*cnt}>>>dfs({tickets[i][1]}, {cnt+1}) 종료, {route}")
                route.pop()
                visited[i] = False
                
    
    dfs("ICN", 0)
    return sorted(answers)[0]