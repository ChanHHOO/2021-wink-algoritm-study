import sys
from collections import deque

n = int(sys.stdin.readline())

def dfs(graph, stack, distances):

    visit = [False for _ in range(0,n+1)]

    while stack:
        node, distance = stack.pop()

        if visit[node] == False:

            visit[node] = True

            for nextNode, nextDistance in graph[node].items():
                
                if visit[nextNode] == False:

                    distances[nextNode - 1] = distance + nextDistance

                    stack.append((nextNode, distance + nextDistance))




graph = {i : {} for i in range(1, n+1)}

for _ in range(n-1):
    
    a, b, c = map(int, sys.stdin.readline().split())

    graph[a][b] = c

    graph[b][a] = c

distances = [0 for _ in range(n)]

stack = [(1, 0)]

dfs(graph, stack, distances)
stack = [(distances.index(max(distances))+1, 0)]
distances = [0 for _ in range(n)]
dfs(graph, stack, distances)

print(max(distances))
