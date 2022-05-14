import sys
from collections import deque

allow = [(-1,0), (0, 1), (1, 0), (0, -1)]

def bfs(n, m, ci, cj, visit):

    q = deque()

    q.append((ci, cj))

    while q:

        node = q.popleft()

        if visit[node[0]][node[1]] == False and graph[node[0]][node[1]] == 1:

            visit[node[0]][node[1]] = True

            for i in range(4):

                if 0 <= node[0] + allow[i][0] < n and 0 <= node[1] + allow[i][1] < m:
                    
                    if graph[node[0] + allow[i][0]][node[1] + allow[i][1]] == 1:

                        q.append((node[0] + allow[i][0] ,node[1] + allow[i][1]))
        




t = int(sys.stdin.readline())

answers = []

for _ in range(t):
    
    m, n, k = map(int, sys.stdin.readline().split())

    visit = [[False for _ in range(m)] for _ in range(n)]

    graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    answer = 0
    for i in range(n):

        for j in range(m):

            if visit[i][j] == False and graph[i][j] == 1:

                bfs(n, m, i, j, visit)

                answer += 1

    answers.append(answer)

for i in range(t):
    print(answers[i])



    
