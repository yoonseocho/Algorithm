import sys
import math

input = sys.stdin.readline

book = input().strip()
word = input().strip()

book = book.replace(word, "*")

print(book.count("*"))