def solution(numbers, target):
    n = len(numbers)
    answer = 0
    indent = "  "
    def dfs(curr_sum, cnt):
        nonlocal answer
        #print(indent*cnt + f"ENTER: curr_sum={curr_sum}, cnt={cnt}")
        if cnt == n:
            if curr_sum == target:
                answer += 1
            #print(indent*cnt + f"END: curr_sum={curr_sum}, cnt={cnt}, answer = {answer}")
            return
        
        dfs(curr_sum - numbers[cnt], cnt + 1)
        dfs(curr_sum + numbers[cnt], cnt + 1)
    dfs(0, 0)
    
    return answer