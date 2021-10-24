import sys

def bfs(color, i, j, sw):
    
    q = [(i, j)]

    while q:
        node = q.pop(0)
        
        if sw == 0:
            if visit[node[0]][node[1]] == False:
                visit[node[0]][node[1]] = True
                for k in range(4):
                    if 0 <= allow[k][0] + node[0] < n and 0 <= allow[k][1] + node[1] < n:
                        if color == 'B' and graph[node[0] + allow[k][0]][node[1] + allow[k][1]] == 'B':
                            q.append((node[0] + allow[k][0], node[1] + allow[k][1]))
                            
                        if color != "B" and graph[node[0] + allow[k][0]][node[1] + allow[k][1]] != 'B':
                            q.append((node[0] + allow[k][0], node[1] + allow[k][1]))
        else:
            if nvisit[node[0]][node[1]] == False:
                nvisit[node[0]][node[1]] = True
                for k in range(4):
                    if 0 <= allow[k][0] + node[0] < n and 0 <= allow[k][1] + node[1] < n:
                        if graph[node[0] + allow[k][0]][node[1] + allow[k][1]] == color:
                            q.append((node[0] + allow[k][0], node[1] + allow[k][1]))


n = int(input())

graph = []

allow = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for _ in range(n):
    graph.append(list(sys.stdin.readline()))

visit = [[False for _ in range(n)] for _ in range(n)]

nvisit = [[False for _ in range(n)] for _ in range(n)]

c, nc = 0, 0

for i in range(n):

    for j in range(n):

        if visit[i][j] == False:
            bfs(graph[i][j],i ,j, 0)
            c += 1
        if nvisit[i][j] == False:
            bfs(graph[i][j],i ,j, 1)
            nc += 1
print(nc, c)