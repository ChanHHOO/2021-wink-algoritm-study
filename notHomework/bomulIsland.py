from lib2to3.pgen2 import grammar
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):

    tmp = list(sys.stdin.readline())

    graph.append(tmp[:-1])

allow = [(-1, 0), (0, 1), (1, 0), (0, -1)]

answer = 0

def bfs(ci, cj):

    q = deque()

    visit = [[False for _ in range(m)] for _ in range(n)]

    deepGraph = [[0 for _ in range(m)] for _ in range(n)]

    q.append((ci, cj))

    deepGraph[ci][cj] = 1

    deep = 0

    while q:

        node = q.popleft()

        if visit[node[0]][node[1]] == False and graph[node[0]][node[1]] == 'L':

            visit[node[0]][node[1]] = True

            for i in range(4):

                if 0 <= node[0] + allow[i][0] < n and 0 <= node[1] + allow[i][1] < m:

                    if graph[node[0] + allow[i][0]][node[1] + allow[i][1]] == 'L':
                        
                        if deepGraph[node[0] + allow[i][0]][node[1] + allow[i][1]] == 0:

                            deepGraph[node[0] + allow[i][0]][node[1] + allow[i][1]] = deepGraph[node[0]][node[1]] + 1

                        else:

                            deepGraph[node[0] + allow[i][0]][node[1] + allow[i][1]] = min(deepGraph[node[0]][node[1]] + 1, deepGraph[node[0] + allow[i][0]][node[1] + allow[i][1]])

                        q.append((node[0] + allow[i][0], node[1] + allow[i][1]))

                        deep = max(deep, deepGraph[node[0] + allow[i][0]][node[1] + allow[i][1]])


    return deep

deep = 0
for i in range(n):
    
    for j in range(m):

        if graph[i][j] == 'L':
            deep = bfs(i, j)

        if answer <= deep:

            answer = deep

print(answer - 1)