import sys

input = sys.stdin.readline

def dfs(day): # 오늘 기준으로 최대 수익을 뽑아내는 함수
    if day >= n:
        return 0
    
    if day in memo:
        return memo[day]
    
    result = dfs(day + 1)
    if day + period[day] <= n:
        result = max(result, money[day] + dfs(day + period[day]))
    
    memo[day] = result
    return result

    
n = int(input())

period = []
money = []
for _ in range(n):
    t, p = map(int, input().split())
    period.append(t)
    money.append(p)

memo = {}

print(dfs(0))