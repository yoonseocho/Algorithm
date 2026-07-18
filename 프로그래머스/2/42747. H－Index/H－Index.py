def solution(citations):
    n = len(citations)
    h_index = 0
    h_indexs = []
    
    while h_index <= n:
        cnt1 = 0
        
        for citation in citations:
            if citation >= h_index:
                cnt1 += 1
        
        if cnt1 >= h_index:
            h_indexs.append(h_index)
        
        h_index += 1
    
    return max(h_indexs) if h_indexs else 0
            
    