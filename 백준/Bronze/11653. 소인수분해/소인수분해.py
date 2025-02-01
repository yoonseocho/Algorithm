def prime_factorization(x):
    answer = []
    k = 2
    while x > 1:
        while x % k == 0:
            answer.append(k)
            x //= k
        k += 1
    return answer

N = int(input())
answer_list = prime_factorization(N)
print('\n'.join(map(str, answer_list)))