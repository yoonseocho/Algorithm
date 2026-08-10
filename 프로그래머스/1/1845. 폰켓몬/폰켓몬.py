def solution(nums):
    n = len(nums)
    can_get = n // 2
    
    unique_nums = set(nums)
    
    if can_get <= len(unique_nums):
        return can_get
    else:
        return len(unique_nums)