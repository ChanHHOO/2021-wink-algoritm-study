import sys
from collections import deque

allow = [[-1, 0],[0, 1], [1, 0], [0, -1]]

n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    tmp = list(sys.stdin.readline())
    graph.append(tmp[:-1])

visit = [[False] * m for _ in range(n)]


def dfs(ci, cj, alphabet):
    
    stack = deque()

    stack.append([(ci, cj), (-1, -1)])

    while stack:
        
        node = stack.popleft()

        if visit[node[0][0]][node[0][1]] == False:
            
            visit[node[0][0]][node[0][1]] = True

            tmp = []

            for i in range(4):

                if 0 <= node[0][0] + allow[i][0] < n and 0 <= node[0][1] + allow[i][1] < m:
                    if (node[0][0] + allow[i][0], node[0][1] + allow[i][1]) != (node[1][0], node[1][1]) and visit[node[0][0] + allow[i][0]][node[0][1] + allow[i][1]] == True:
                        if graph[node[0][0] + allow[i][0]][node[0][1] + allow[i][1]] == alphabet:
                            return 1
                    elif visit[node[0][0] + allow[i][0]][node[0][1] + allow[i][1]] == False and graph[node[0][0] + allow[i][0]][node[0][1] + allow[i][1]] == alphabet:
                        tmp.append([(node[0][0] + allow[i][0], node[0][1] + allow[i][1]), (node[0][0], node[0][1])])
            stack.extendleft(tmp)




for i in range(n):

    for j in range(m):

        if visit[i][j] == False:

            if dfs(i, j, graph[i][j]):
                print("Yes")
                exit()
else:
    print("No")