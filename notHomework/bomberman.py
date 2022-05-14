import sys 

r, c, n = map(int, sys.stdin.readline().split())

graph = []

for _ in range(r):
    tmp = list(sys.stdin.readline())
    graph.append(tmp[:-1])

cnt = 0

allow = [(1, 0), (0, 1), (-1, 0), (0, -1)]

booms = []

while cnt <= n:

    if cnt % 2 == 1:

        if booms:

            for i in range(len(booms)):

                graph[booms[i][0]][booms[i][1]] = '.'

                for j in range(4):

                    if 0 <= booms[i][0] + allow[j][0] < r and 0 <= booms[i][1] + allow[j][1] < c:

                        graph[booms[i][0] + allow[j][0]][booms[i][1] + allow[j][1]] = '.'

            booms = []

        
        for i in range(r):
            
            for j in range(c):

                if graph[i][j] == 'O':
                    booms.append((i, j))
        
    else:

        if cnt != 0:

            for i in range(r):

                for j in range(c):

                    graph[i][j] = 'O'

    cnt += 1

for i in range(r):

    a = ''.join(graph[i])

    print(a)
