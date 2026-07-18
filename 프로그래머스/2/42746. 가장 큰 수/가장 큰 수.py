def solution(numbers):
    numbers_str = list(map(str, numbers))
    
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    
    
    return "0" if numbers_str[0] == "0" else ''.join(numbers_str)
    