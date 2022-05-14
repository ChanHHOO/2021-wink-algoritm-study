import sys
from collections import deque
def bfs(networks, n):

    q = deque()

    q.append(1)

    visit = [False for i in range(n+1)]

    answer = 0

    while q:

        node = q.popleft()

        if visit[node] == False:
            visit[node] = True
            answer += 1
            for i in range(len(networks[node])):
                q.append(networks[node][i])
    
    print(answer-1)






n = int(input())
networks = {i:[] for i in range(1, n+1)}
relations = int(input())

for i in range(relations):

    a, b = map(int, sys.stdin.readline().split())


    networks[a].append(b)
    networks[b].append(a)
bfs(networks, n)