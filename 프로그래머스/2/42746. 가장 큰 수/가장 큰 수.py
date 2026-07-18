def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    
    numbers_str = list(map(str, numbers))
    
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    
    return ''.join(numbers_str)
    