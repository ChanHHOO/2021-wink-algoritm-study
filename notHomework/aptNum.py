import sys

def bfs(start):
    q = [start]
    allow = [[1, 0],[0,1],[-1, 0],[0, -1]]
    size = 0
    while q:
        node = q.pop(0)
        if visit[node[0]][node[1]] == False and apts[node[0]][node[1]] == 1:
            visit[node[0]][node[1]] = True
            size += 1
            for i in range(4):
                if apts[node[0] + allow[i][0]][node[1] + allow[i][1]] == 1 and visit[node[0]+ allow[i][0]][node[1] + allow[i][1]] == False:
                    q.append( (node[0] + allow[i][0], node[1]+allow[i][1]) )

    return size




n = int(input())

visit = [[False for _ in range(n+1)] for _ in range(n+1)]

apts = []

answer = []

cnt = 0

for i in range(n):
    tmp = sys.stdin.readline()
    apts.append(list(map(int, tmp[:-1])))
    apts[-1].append(0)
apts.append([0 for _ in range(n+1)])
for i in range(n):
    for j in range(n):
        if apts[i][j] == 1 and visit[i][j] == False:
            cnt += 1
            answer.append(bfs((i,j)))
print(cnt)
answer.sort()
for i in range(len(answer)):
    print(answer[i])