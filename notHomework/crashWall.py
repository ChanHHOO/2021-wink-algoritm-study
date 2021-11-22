import sys 
import copy
allow = [[-1,0], [0,1], [1,0], [0,-1]]

n, m = map(int, sys.stdin.readline().split(" "))

graph = []

visit = [[False]*m for _ in range(n)]

answer = -1

def dfs( graphCopy, visit):
    stack = [(0, 0)]
    while stack:
        node = stack.pop(0)
        if visit[node[0]][node[1]] == False:
            visit[node[0]][node[1]] = True
            for i in range(4):
                if 0 <= node[0] + allow[i][0] < n and 0 <= node[1] + allow[i][1] < m:
                    if graphCopy[node[0] + allow[i][0]][node[1] + allow[i][1]] != 1:
                        if graphCopy[node[0] + allow[i][0]][node[1] + allow[i][1]] == 0:
                            graphCopy[node[0] + allow[i][0]][node[1] + allow[i][1]] = graphCopy[node[0]][node[1]] - 1
                        elif graphCopy[node[0] + allow[i][0]][node[1] + allow[i][1]] != 1:
                            graphCopy[node[0] + allow[i][0]][node[1] + allow[i][1]] = max(graphCopy[node[0]][node[1]] - 1, graphCopy[node[0]+allow[i][0]][node[1]+allow[i][1]])
                        stack.append((node[0] + allow[i][0], node[1] + allow[i][1]))
wallPositions = []

for i in range(n):

    a = list(sys.stdin.readline())
    for j in range(len(a[:-1])):
        if a[j] == '1':
            a[j] = 1
            wallPositions.append((i, j))
        else:
            a[j] = 0

    graph.append(a[:-1])

for k in range(len(wallPositions)):
    graph[wallPositions[k][0]][wallPositions[k][1]] = 0
    graphCopy = copy.deepcopy(graph)
    visit = [[False]*m for _ in range(n)]
    
    
    dfs(graphCopy, visit)
    if graphCopy[n-1][m-1] != 0:
        answer = answer if abs(graphCopy[n-1][m-1]) < answer else graphCopy[n-1][m-1]
    graph[wallPositions[k][0]][wallPositions[k][1]] = 1
    

if answer != -1:
    answer = (answer * -1) + 1
print(answer)