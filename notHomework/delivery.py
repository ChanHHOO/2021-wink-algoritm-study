import sys
import heapq
import math 

n, m = map(int, sys.stdin.readline().split())

graph = {node:{} for node in range(1, n+1)}

distances = {node : math.inf for node in graph}

distances[1] = 0

for _ in range(m):

    a, b, c = map(int, sys.stdin.readline().split())

    try:
        if graph[a][b] != None:
            graph[a][b] = min(graph[a][b], c)
    except:
        graph[a][b] = c

    try:
        if graph[b][a] != None:
            graph[b][a] = min(graph[b][a], c)
    except:
        graph[b][a] = c

q = []

heapq.heappush(q, (distances[1], 1))

while q:
    current_distance, current_destination = heapq.heappop(q)
    
    if distances[current_destination] < current_distance:
        continue
    
    for new_destination, new_distance in graph[current_destination].items():
        
        distance = current_distance + new_distance

        if distance < distances[new_destination]:

            distances[new_destination] = distance

            heapq.heappush(q, (distance, new_destination))

print(distances[n])