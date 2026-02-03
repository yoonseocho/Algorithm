def solution(n):
    start, end = 1, 1
    total_sum = 1
    cnt = 0
    while start <= n:
        if total_sum < n:
            end += 1
            total_sum += end
        elif total_sum == n:
            cnt += 1
            total_sum -= start
            start += 1
        else:
            total_sum -= start
            start += 1
    return cnt