import sys
import math
from collections import deque

n, m, b = map(int, sys.stdin.readline().split(" "))

graph = []

blockCnt = b

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    blockCnt += sum(tmp)
    graph.append(tmp)

maxHeight = 0

while(True):
    if m * n * maxHeight > blockCnt:
        maxHeight -= 1
        break
    maxHeight += 1

answerTime = math.inf
answerHeight = 0

for targetHeight in range(maxHeight+1):
    tmpTime = 0
    for j in range(n):

        for k in range(m):

            if graph[j][k] > targetHeight:
                tmpTime += ((graph[j][k] - targetHeight) * 2)
            else:
                tmpTime += (targetHeight - graph[j][k])
    if tmpTime < answerTime:
        answerTime = tmpTime
        answerHeight = targetHeight

print(answerTime, answerHeight)
