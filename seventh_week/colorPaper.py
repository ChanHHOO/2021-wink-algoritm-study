n = int(input())
position = []
graph = [[0 for i in range(102)] for j in range(102)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(tmp[0], tmp[0]+10):

        for k in range(tmp[1]-1, tmp[1]+9):
            graph[99-k][j+1] = 1
    # for q in range(27):
    #     print(graph[q])

answer = 0
for i in range(102):
    for j in range(102):
        if graph[i][j] == 1:
            if graph[i-1][j] == 0:
                answer += 1
            if graph[i+1][j] == 0:
                answer += 1
            if graph[i][j-1] == 0:
                answer += 1
            if graph[i][j+1] == 0:
                answer += 1
print(answer)
            
