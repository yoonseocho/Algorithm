from collections import defaultdict

def solution(numbers, target):
    # dp[i]: 지금까지 처리한 숫자들로 합 i를 만드는 경우의 수
    dp = {}
    dp[0] = 1
    
    for num in numbers:
        new_dp = defaultdict(int)
        for s, cnt in dp.items():
            new_dp[s+num] += cnt
            new_dp[s-num] += cnt
        dp = new_dp
    
    
    return dp[target]