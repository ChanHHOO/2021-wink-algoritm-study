import sys

n = int(sys.stdin.readline())

words = []

for _ in range(n):
    tmp = sys.stdin.readline()
    words.append(tmp[:-1])
words = list(set(words))
words.sort()
words.sort(key=lambda x : len(x))

for i in words:
    print(i)