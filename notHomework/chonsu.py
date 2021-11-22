from collections import deque
import sys
def bfs(graph, a, b, n):
    visit = [False for _ in range(1, n+1)]
    q = deque()
    q.append(a)
    while q:
        print(q)
        node = q.pop()
        if visit[node - 1] == False:
            visit[node-1] = True
            q.extend(graph[node])


n = int(sys.stdin.readline())

a, b = map(int, sys.stdin.readline().split(" "))

m = int(sys.stdin.readline())

graph = {}

for i in range(1, n+1):
    graph[i] = []

for i in range(m):
    x, y = map(int, sys.stdin.readline().split(" "))

    graph[x].append(y)
    graph[y].append(x)
bfs(graph, a, b, n)