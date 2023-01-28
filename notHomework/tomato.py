from re import A
import sys
import math
from collections import deque

allows = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(graph, positions, n, m):
 
    q = deque()
    for i in range(len(positions)):
        q.append(positions[i])

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + allows[i][1]
            nx = cx + allows[i][0]
            if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] != -1:
                if graph[ny][nx] > graph[cy][cx] + 1 or graph[ny][nx] == 0:
                    q.append((ny, nx))
                    graph[ny][nx] = graph[cy][cx] + 1

input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = []

positions = []

for i in range(m):
    tmp = list(map(int, input().split(" ")))
    for j in range(n):
        if tmp[j] == 1:
            positions.append((i, j))
    graph.append(tmp)


bfs(graph, positions, n, m)
# for startY, startX in positions:


maxVal = 0
sw = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            sw = 1
            maxVal = 0
            break
        if graph[i][j] > maxVal:
            maxVal = graph[i][j]
    if sw:
        break
print(maxVal-1)