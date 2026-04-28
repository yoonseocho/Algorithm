def is_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    prime_num = set()
    visited = [False] * len(numbers)
    
    def dfs(curr_str):
        if curr_str:
            num = int(curr_str)
            if is_prime(num):
                prime_num.add(num)
                
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(curr_str+numbers[i])
                visited[i] = False
    dfs("")
    return len(prime_num)