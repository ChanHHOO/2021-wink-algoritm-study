import sys
import math
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split(" "))

graph = {}

for i in range(1, n+1):
    graph[i] = []
for i in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)

visit = [False for _ in range(n)]

distance = [math.inf for _ in range(n)]

distance[x-1] = 0

q = deque()
q.append(x-1)
minIdx = 300001

while q:
    node = q.popleft()
    if visit[node] == False:
        visit[node] = True
        for i in range(len(graph[node+1])):
            q.append(graph[node+1][i]-1)
            distance[graph[node+1][i]-1] = min(distance[graph[node+1][i]-1], distance[node] + 1)
answer = []
for i in range(len(distance)):
    if distance[i] == k:
        answer.append(i+1)
print(distance)
if answer:
    for i in range(len(answer)):
        print(answer[i])
else:
    print(-1)