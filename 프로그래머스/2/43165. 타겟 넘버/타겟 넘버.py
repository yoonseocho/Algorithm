def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(curr_sum, cnt):
        nonlocal answer
        if cnt == n:
            if curr_sum == target:
                answer += 1
            return
        
        dfs(curr_sum + numbers[cnt], cnt + 1)
        dfs(curr_sum - numbers[cnt], cnt + 1)

    dfs(0, 0)
    
    return answer