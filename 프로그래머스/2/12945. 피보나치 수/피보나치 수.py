def solution(n):
    memo = {0:0, 1:1}
    
    if n == 0 or n ==1:
        return memo[n]
    
    for i in range(2, n+1):
        memo[i] = memo[i-2] + memo[i-1]
    
    return memo[n] % 1234567