def solution(n, k):
    cnt = 0
    
    def get_k_num(n, k):
        k_num = []
        
        while n > 0:
            res = n % k
            k_num.append(res)

            n //= k
        
        return ''.join(map(str, k_num[::-1]))
        
    def is_prime(num):
        if num < 2:
            return False
        
        for div in range(2, int(num**0.5)+1):
            if num % div == 0:
                return False
        
        return True
    
    # k진수로 바꾸기
    k_num_str = get_k_num(n, k)

    # 소수 찾기
    candidates = [int(num) for num in k_num_str.split('0') if num != '']
    
    for candidate in candidates:
        if is_prime(candidate):
            cnt += 1
    
    return cnt