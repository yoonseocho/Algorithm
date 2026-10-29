def solution(numbers, target):
    n = len(numbers)
    ans = 0
    
    def dfs(curr_sum, i):
        nonlocal ans
        if i == n:
            if curr_sum == target:
                ans += 1
            return
        
        dfs(curr_sum + numbers[i], i+1)
        dfs(curr_sum - numbers[i], i+1)

    dfs(0, 0)
    
    return ans