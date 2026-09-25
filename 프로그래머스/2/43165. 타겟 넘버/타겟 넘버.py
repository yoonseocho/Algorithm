def solution(numbers, target):
    answer = 0
    def dfs(curr_sum, cnt):
        nonlocal answer
        if cnt == len(numbers):
            if curr_sum == target:
                answer += 1
            return
                
        dfs(curr_sum + numbers[cnt], cnt+1)
        dfs(curr_sum - numbers[cnt], cnt+1)
        
    dfs(0, 0)
    
    return answer