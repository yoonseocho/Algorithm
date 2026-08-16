def solution(n, times):
    m = len(times)
    l, r = 1, (max(times) * n)
    
    def check(num):
        cnt = 0
        for time in times:
            cnt += (num // time)
        return cnt
    
    while l < r:
        mid = (l+r) // 2
        
        num = check(mid)
        if num >= n:
            r = mid
        else:
            l = mid + 1
    return l
    