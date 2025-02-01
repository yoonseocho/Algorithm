import sys
input = sys.stdin.readline

def count_k(n, k):
    result = 0
    power = k
    while power <= n:
        result += n // power
        power *= k
    return result

n, m = map(int, input().rstrip().split())

two = count_k(n, 2) - count_k(m, 2) - count_k(n-m, 2)
five = count_k(n, 5) - count_k(m, 5) - count_k(n-m, 5)

print(min(two ,five))

