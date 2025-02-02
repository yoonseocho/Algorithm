import math

for _ in range(int(input())):
    test_case = list(map(int, input().split()))
    test_case.pop(0)
    result = 0
    for i in range(len(test_case)-1):
        for j in range(i+1, len(test_case)):
            result += math.gcd(test_case[i], test_case[j])
    print(result)