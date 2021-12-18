# 5
# 7
# 1 2 2
# 1 3 3
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

import sys

import math

import heapq

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

graph = {}

for i in range(1, n+1):
    graph[i] = {}

for _ in range(m):

    a, b, c = map(int, sys.stdin.readline().split())

    graph[a] = (b,c)

print(graph)

start, finish = map(int, sys.stdin.readline().split())

distance = [math.inf for _ in range(n)]

q = []

heapq.heappush(q, (0, start))

distance[start-1] = 0

while q:
    dist, node = heapq.heappop(q)
    if distance[node-1] < dist:
        continue
    for next in graph[node].items()