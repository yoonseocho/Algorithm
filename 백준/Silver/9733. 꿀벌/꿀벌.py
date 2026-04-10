import sys
import math

data = sys.stdin.read().split()

tasks = ["Re", "Pt", "Cc", "Ea", "Tb", "Cm", "Ex"]
counts = {task:0 for task in tasks}

total_count = len(data)

for d in data:
    if d in tasks:
        counts[d] += 1

for task in tasks:
    ratio = counts[task] / total_count
    print(f"{task} {counts[task]} {ratio:.2f}")

print(f"Total {total_count} 1.00")