def devide_team(visited):
    global min_diff
    
    start_score = 0
    link_score = 0

    for i in range(n):
        for j in range(i+1, n):
            if visited[i] and visited[j]:
                start_score += s[i][j] + s[j][i]
            elif not visited[i] and not visited[j]:
                link_score += s[i][j] + s[j][i]

    diff = abs(start_score - link_score)

    if diff == 0:
        print(0)
        exit()

    min_diff = min(min_diff, diff)
    
    

def dfs(idx, current_people):
    global visited

    if current_people == n // 2:
        devide_team(visited)
        return
    
    for i in range(idx, n):
        if not visited[i]:
            current_people += 1
            visited[i] = True
            dfs(i + 1, current_people)
            visited[i] = False
            current_people -= 1

    
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
member_list = [i for i in range(n)]

min_diff = float('inf')
min_list = []

visited = [False] * n
visited[0] = True
dfs(1, 1)

print(min_diff)