import sys
input = sys.stdin.readline
sum = 0
credit_sum = 0

for _ in range(20):
    each_gpa = input().rstrip().split()
    credits = float(each_gpa[1])
    grade = each_gpa[2]

    if grade != "P":
        credit_sum += credits

    if grade == "A+":
        sum += credits * 4.5
    elif grade == "A0":
        sum += credits * 4.0
    elif grade == "B+":
        sum += credits * 3.5
    elif grade == "B0":
        sum += credits * 3.0
    elif grade == "C+":
        sum += credits * 2.5
    elif grade == "C0":
        sum += credits * 2.0
    elif grade == "D+":
        sum += credits * 1.5
    elif grade == "D0":
        sum += credits * 1.0
    elif grade == "F":
        sum += credits * 0.0

print(sum / credit_sum)