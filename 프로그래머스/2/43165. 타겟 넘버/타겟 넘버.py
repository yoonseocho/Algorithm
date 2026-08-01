def solution(numbers, target):
    n = len(numbers)
    answer = 0
    
    def dfs(curr_sum, cnt):
        # print(f"{"    "*cnt} >>> dfs({curr_sum}, {cnt}) 시작")
        nonlocal answer
        if cnt == n:
            if curr_sum == target:
                answer += 1
                # print(f"{"    "*cnt} >>> dfs({curr_sum}, {cnt}) 끝, answer={answer}")
            return
        
        dfs(curr_sum + numbers[cnt], cnt+1)
        dfs(curr_sum - numbers[cnt], cnt+1)
    
    dfs(0, 0)
    
    return answer