import sys

word = sys.stdin.readline().strip()

word = word.replace("c=", " ").replace("c-", " ").replace("dz=", " ").replace("d-", " ").replace("lj", " ").replace("nj", " ").replace("s=", " ").replace("z=", " ")
print(len(word))