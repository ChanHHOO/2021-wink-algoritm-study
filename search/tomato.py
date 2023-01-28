import sys
from collections import deque

allow = [[0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]
n, m, h = map(int, sys.stdin.readline().split())
def bfs(q, graph, visit):

    while q:
        # for i in range(2):
        #     for j in range(3):
        #         print(graph[i][j])
        # print('========', q)
        
        k, i, j = q.popleft()
        
        if visit[k][i][j] == False:

            visit[k][i][j] = True

            for a in range(6):
                
                if 0 <= k + allow[a][0] < h and 0 <= i + allow[a][1] < m and 0 <= j + allow[a][2] < n and graph[k + allow[a][0]][i + allow[a][1]][j + allow[a][2]] == 0:

                    graph[k + allow[a][0]][i + allow[a][1]][j + allow[a][2]] = graph[k][i][j] + 1

                    q.append((k + allow[a][0], i + allow[a][1], j + allow[a][2]))

graph = [[] for _ in range(h)]

count = 0

i = 0
q = deque()
for _ in range(m * h):
    tmp = list(map(int, sys.stdin.readline().split()))
    if count == m:
        count = 0
        i+=1 
    
    graph[i].append(tmp)
    for j in range(n):
        if tmp[j] == 1:
            q.append((i, len(graph[i])-1, j))
    count += 1

visit = [[[False for _ in range(n)] for _ in range(m)] for _ in range(h)]

bfs(q, graph, visit)

maxVal = 0
for k in range(h):

    for i in range(m):

        for j in range(n):

            if graph[k][i][j] == 0:
                print(-1)
                exit()
            if maxVal <= graph[k][i][j]:
                maxVal = graph[k][i][j]

if maxVal != 1:
    print(maxVal - 1)
else:
    print(0)