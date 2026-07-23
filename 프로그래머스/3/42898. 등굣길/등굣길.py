def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for y, x in puddles:
        dp[x][y] = -1
    
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i==1 and j==1) or dp[i][j] == -1:
                continue
            
            from_top = dp[i-1][j] if dp[i-1][j] != -1 else 0
            from_left = dp[i][j-1] if dp[i][j-1] != -1 else 0
            
            dp[i][j] = (from_top + from_left) % 1000000007
    
    return dp[n][m]