def solution(numbers, target):
    answer = 0
    indent = "   "
    def dfs(curr_sum, depth):
        nonlocal answer
        if depth == len(numbers):
            if curr_sum == target:
                answer += 1
            return
        
        dfs(curr_sum + numbers[depth], depth+1)
        dfs(curr_sum - numbers[depth], depth+1)
    
    dfs(0, 0)
    
    return answer