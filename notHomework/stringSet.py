import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

stringSet = []

for _ in range(n):
    tmp = sys.stdin.readline()
    heapq.heappush(stringSet, tmp[:-1])

inputStrings = []
answer = 0
for _ in range(m):

    word = sys.stdin.readline()
    if word[:-1] in stringSet:
        answer += 1




print(answer)

