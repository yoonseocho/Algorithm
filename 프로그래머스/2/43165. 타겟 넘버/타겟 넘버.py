def dfs(index, current_sum, numbers, target):
    if index == len(numbers):
        if current_sum == target:
            return 1
        else:
            return 0
    left = dfs(index + 1, current_sum + numbers[index], numbers, target)
    right = dfs(index + 1, current_sum - numbers[index], numbers, target)
    
    return left + right

def solution(numbers, target):
    return dfs(0, 0, numbers, target)