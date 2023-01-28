import sys
from collections import deque

allow = [(-1,0), (0, 1), (1, 0), (0, -1)]

def bfs(graph, i, j, n, m):
    q = deque()
    q.append((i, j))
    while q:

        node = q.popleft()

        if(graph[node[0]][node[1]] == 1):
            graph[node[0]][node[1]] += 1
            for allowY, allowX in allow:
                if 0 <= allowY + node[0] < n and 0 <= allowX + node[1] < m and graph[allowY + node[0]][allowX + node[1]] == 1:
                    q.append((allowY + node[0], allowX + node[1]))


input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    
    m, n, k = map(int, input().split(" "))

    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split(" "))
        graph[y][x] = 1
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j, n, m)
                answer += 1

    print(answer)