N, K = map(int, input().split())

people = list(range(1,N+1))
current_idx = 0
result = []

for _ in range(N):
    current_idx = (current_idx + K-1) % len(people)
    result.append(people.pop(current_idx))
        
print("<"+', '.join(map(str, result))+">")