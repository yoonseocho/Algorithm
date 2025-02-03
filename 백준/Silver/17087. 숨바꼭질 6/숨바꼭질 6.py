import math
from functools import reduce

def gcd_of_distances(subin, sisters):
    distances = [abs(subin - s) for s in sisters]
    return reduce(math.gcd, distances)

n, s = map(int, input().split())
sisters = list(map(int, input().split()))
print(gcd_of_distances(s, sisters))