import math
import sys
import heapq

def dijkstra(graph, dist, start, target):
    q = [(0, start)]
    dist[start] = 0
    while q:
        cDist, cNode = heapq.heappop(q)
        if cDist > dist[cNode]:
            continue
        for nDist, nNode in graph[cNode]:
            distance = cDist + nDist
            if distance < dist[nNode]:
                dist[nNode] = distance
                heapq.heappush(q, (distance, nNode))
    print(dist[target])

input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = {i:[] for i in range(0, n+1)}

for _ in range(m):
    a, b, v = map(int, input().split(" "))
    graph[a].append((v, b))
    graph[b].append((v, a))

dist = [math.inf] * (n + 1)

start, target = map(int, input().split(" "))
# print(graph)
dijkstra(graph, dist, start, target)