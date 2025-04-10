import sys
from itertools import combinations

input = sys.stdin.readline


def solution():
    global min_diff
    
    comb = list(combinations(member_list, n//2))

    for team in comb:
        start_team = list(team)
        link_team = list(set(member_list) - set(start_team))

        start_score = 0
        link_score = 0

        for i, j in combinations(start_team, 2):
            start_score += s[i][j] + s[j][i]
        for i, j in combinations(link_team, 2):
            link_score += s[i][j] + s[j][i]

        min_diff = min(min_diff, abs(start_score - link_score))

        if min_diff == 0:
            break
    return min_diff

n= int(input())
s = [list(map(int, input().split())) for _ in range(n)]

member_list = [i for i in range(n)]
min_diff = float('inf')

print(solution())