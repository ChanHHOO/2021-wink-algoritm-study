import math
import sys
import heapq

def dijkstra(graph, dist, d):
    q = [(0, 0)]
    dist[0] = 0
    while q:
        cDist, cNode = heapq.heappop(q)
        if cDist > dist[cNode]:
            continue
        for nDist, nNode in graph[cNode]:
            if nNode <= d:
                distance = cDist + nDist
                if distance < dist[nNode]:
                    dist[nNode] = distance
                    heapq.heappush(q, (distance, nNode))
    print(dist[d])

input = sys.stdin.readline

n, d = map(int, input().split(" "))

graph = {i:[] for i in range(0, d+1)}

for i in range(0, d+1):
    graph[i].append((1, i+1))

for _ in range(n):
    a, b, v = map(int, input().split(" "))
    if b <= d:
        graph[a].append((v, b))

dist = [math.inf] * (d + 1)

# print(graph)

dijkstra(graph, dist, d)