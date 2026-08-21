def solution(brown, yellow):
    def find_candidates(yellow):
        candidate = []
        for i in range(1, int(yellow**0.5)+1):
            if yellow % i != 0:
                continue
            j = yellow // i
            if i <= j:
                candidate.append((j+2, i+2))
        return candidate
    
    possible_cases = find_candidates(yellow)
    print(possible_cases)
    for i, j in possible_cases:
        if i * j - yellow == brown:
            return [i, j]
                