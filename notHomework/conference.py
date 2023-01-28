import sys
from collections import deque

n = int(sys.stdin.readline())

conferences = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    conferences.append((a, b))
conferences.sort(key = lambda x : (x[0], x[1]))
answers = [conferences[0]]
for i in range(1, n):
    start, end = conferences[i]
    if end < answers[-1][1]:
        answers.pop()
        answers.append((start, end))
    elif start >= answers[-1][1]:
        answers.append((start, end))
print(len(answers))

"""
0 6
1 4
2 13
3 5
3 8
5 7
5 9
6 10
8 11
8 12
12 14
"""