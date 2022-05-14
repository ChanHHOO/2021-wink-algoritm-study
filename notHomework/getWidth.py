from re import L
import sys
from collections import deque

allow = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m, k = map(int, sys.stdin.readline().split())

def dfs(graph, visit, ci, cj):
    
    q = deque()

    q.append((ci, cj))

    width = 0

    while q:

        node = q.popleft()

        if visit[node[0]][node[1]] == False and graph[node[0]][node[1]] == 0:

            visit[node[0]][node[1]] = True
            width += 1
            for i in range(4):

                if 0 <= allow[i][0] + node[0] < n and 0 <= allow[i][1] + node[1] < m:

                    if graph[allow[i][0] + node[0]][allow[i][1] + node[1]] == 0:

                        q.append((allow[i][0] + node[0], allow[i][1] + node[1]))
    return width

graph = [[0 for _ in range(m)] for _ in range(n)]

visit = [[False for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(y2-y1):

        for j in range(x2-x1):

            graph[y1+i][x1+j] = 1

graph.reverse()

answer = 0

widthes = []

for i in range(n):

    for j in range(m):

        if visit[i][j] == False and graph[i][j] == 0:
            widthes.append(dfs(graph, visit, i, j))
            answer += 1

widthes.sort()

for i in range(len(widthes)):
    widthes[i] = str(widthes[i])

st = " ".join(widthes)

print(answer)

print(st)