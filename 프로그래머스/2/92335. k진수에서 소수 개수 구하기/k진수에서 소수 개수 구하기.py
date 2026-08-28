def solution(n, k):
    cnt = 0
    
    def get_k_num(n, k):
        k_num = []
        
        while n >= k:
            res = n % k
            k_num.append(res)

            n //= k
        
        k_num.append(n)
        return ''.join(map(str, k_num[::-1]))
        
    def slice_by_zero(k_num_str):
        candidates = []
        k_num_cpy = k_num_str[:]
        start = 0
        for i, num in enumerate(k_num_str):
            if num == "0":
                slice = k_num_cpy[start:i]
                if slice != '':
                    candidates.append(int(slice))
                
                start = i+1
            
            else:
                if i == len(k_num_str) -1:
                    slice = k_num_cpy[start:]
                    if slice != '':
                        candidates.append(int(slice))
        return candidates
        
    def is_prime(num):
        if num == 1:
            return False
        
        for div in range(2, int(num**0.5)+1):
            if num % div == 0:
                return False
        
        return True
    
    # k진수로 바꾸기
    k_num_str = get_k_num(n, k)

    # 소수 찾기
    candidates = slice_by_zero(k_num_str)
    
    for candidate in candidates:
        if is_prime(candidate):
            cnt += 1
    
    return cnt