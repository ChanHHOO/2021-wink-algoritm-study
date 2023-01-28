import sys
import heapq
import math

def dijkstra(graph, dist, start):

    dist[start] = 0
    q = [(0, start)]
    
    while q:
        current_dist, current_node = heapq.heappop(q)

        if current_dist > dist[current_node]:
            continue

        for next_dist, next_node in graph[current_node]:
            if current_dist + next_dist < dist[next_node]:
                dist[next_node] = current_dist + next_dist
                heapq.heappush(q, (current_dist + next_dist, next_node))
    # print(dist)
input = sys.stdin.readline

n, m, k, start = map(int, input().rstrip().split())

graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append((1, b))

dist = [math.inf for _ in range(n+1)]

dijkstra(graph, dist, start)
isAns = False
for i in range(1, len(dist)):
    if dist[i] == k:
        isAns = True
        print(i)
if not isAns:
    print(-1)
