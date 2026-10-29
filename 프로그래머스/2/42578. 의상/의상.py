from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    
    for name, cloth_type in clothes:
        clothes_dict[cloth_type] += 1
    
    ans = 1
    for val_cnt in clothes_dict.values():
        ans *= (val_cnt+1)
    
    return ans-1
            
            
    