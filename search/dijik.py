import sys
import heapq
import math

def dijkstra(n, start, end, graph):
    distances = [math.inf] * (n + 1)
    distances[start] = 0

    pq = []
    heapq.heappush(pq, (start, 0))

    while pq:
        node, dis = heapq.heappop(pq)
        if distances[node] < dis:
            continue
        for nextNode, nextDis in graph[node]:
            newDis = nextDis + dis

            if distances[nextNode] > newDis:
                heapq.heappush(pq, (nextNode, newDis))
                distances[nextNode] = newDis
    print(distances[end])

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

graph =  {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
start, end = map(int, sys.stdin.readline().split())
dijkstra(n, start,end, graph)
