import sys
import math
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

canGo = list(map(int, input().split()))
canGo[-1] = 0
graph = {i:[] for i in range(0, n)}

for _ in range(m):
    a, b, c = map(int, input().split())
    if not canGo[a] and not canGo[b]:
        graph[a].append((b, c))
        graph[b].append((a, c))

def dijkstra(n, graph):
    distances = [math.inf] * (n)
    distances[0] = 0

    pq = []
    heapq.heappush(pq, (0, 0))

    while pq:
        curNode, curDis = heapq.heappop(pq)
        if distances[curNode] < curDis:
            continue
        for nextNode, nextDis in graph[curNode]:
            sumVal = nextDis + curDis
            if sumVal < distances[nextNode]:
                heapq.heappush(pq, (nextNode, sumVal))
                distances[nextNode] = sumVal
    if distances[-1] == math.inf:
        print(-1)
        return
    print(distances[-1])

dijkstra(n, graph)