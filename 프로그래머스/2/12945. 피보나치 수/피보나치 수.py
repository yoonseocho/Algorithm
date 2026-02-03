memo = {0:0, 1:1}
def F(n):
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def solution(n):
    return F(n) % 1234567