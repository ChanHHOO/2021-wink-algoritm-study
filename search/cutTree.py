import sys
from collections import deque

treeCnt, target = map(int, sys.stdin.readline().split())

treeList = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(treeList)
results = []
while(low >= high):
    mid = (low + high) // 2
    sum = 0
    for i in range(treeCnt):
        sum += (treeList[i] - mid if treeList[i] - mid > 0 else 0)
    results.append((mid, sum))
    if sum > target:
        low = mid + 1
    elif sum < target:
        high = mid - 1

answer = 0
v = 2000000001
prev = 0
# print(results)
for data in results:
    if(data[1] >= target and data[1] < v):
        v = data[1]
        answer = data[0]
print(answer)