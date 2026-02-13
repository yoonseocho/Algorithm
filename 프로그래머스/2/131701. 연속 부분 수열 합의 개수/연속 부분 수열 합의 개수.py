def solution(elements):
    n = len(elements)
    memo = set()
    
    for i in range(n):
        ssum = 0
        ssum += elements[i]
        memo.add(ssum)
        for j in range(i+1, i+n):
            ssum += elements[j%n]
            memo.add(ssum)
    return len(memo)