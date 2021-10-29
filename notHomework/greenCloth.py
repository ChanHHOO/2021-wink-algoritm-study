import sys
import math

answers = []
cnt = 0
while True:
    n = int(input())
    cnt += 1
    if n == 0:break

    graph = []

    allow = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split(" "))))


    visit = [False for _ in range(n*n)]
    visit[0] = True

    distance = [math.inf for _ in range(n*n)]

    distance[0] = 0
    distance[1] = graph[0][1] + graph[0][0]
    distance[n] = graph[1][0] + graph[0][0]

    while False in visit:
        
        # not visit
        minVal = math.inf
        minIdx = 0
        for i in range(n*n):
            if minVal > distance[i] and visit[i] == False:
                minIdx = i
                minVal = distance[i]
        i = 0 if minIdx < n else minIdx // n
        j = (minIdx % n)
        visit[minIdx] = True
        
        for k in range(4):
            nx = i + allow[k][0]
            ny = j + allow[k][1]
            if 0 <= nx < n and 0 <= ny < n:
                distance[(nx * n) + ny] = min(distance[(nx * n) + ny], distance[(i * n) + j] + graph[nx][ny])
    
    answers.append("Problem "+str(cnt)+": "+str(distance[-1]))
for s in answers:
    print(s)
        
                
            
        


