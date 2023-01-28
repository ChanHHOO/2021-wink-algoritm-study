import sys
import heapq
from collections import deque

allow = [(-1, 0),(1, 0), (0, 1) , (0, -1)]

input = sys.stdin.readline

def bfs(n, startI, startJ, graph):
    q = deque([(startI, startJ)])
    visit = [[False] * (n) for _ in range(n)]
    prev = None
    while q:

        node = q.popleft()

        if visit[node[0]][node[1]] == False:
            visit[node[0]][node[1]] = True
            
            for i in range(4):
                ni = node[0] + allow[i][0]
                nj = node[1] + allow[i][1]
                if 0 <= ni < n and 0 <= nj < n and visit[ni][nj] == False:
                    q.append((ni, nj))
                    graph[ni][nj] = graph[node[0]][node[1]] + 100
                    isP = False; isC = False
                    if prev:
                        if prev in allow[:2]:isP = True
                        if prev in allow[2:]:isP = False
                    if (allow[i][0], allow[i][1]) in allow[:2]: isC = True
                    if (allow[i][0], allow[i][1]) in allow[2:]: isC = False
                    if isP != isC:
                        graph[ni][nj] + 500
                    prev = (allow[i][0], allow[i][1])

graph = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
bfs(3, 0, 0, graph)
print(graph)