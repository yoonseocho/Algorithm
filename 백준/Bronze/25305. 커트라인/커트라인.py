N, k = map(int, input().split())
grade = map(int, input().split())
print(sorted(grade)[-k])