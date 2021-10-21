import sys
def bfs(n, x, y, dx, dy):
    visit = [[False for _ in range(n)] for _ in range(n)]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    
    q = [(x, y)]
    cnt = 0
    sw = 0
    while q:
        node = q.pop(0)
        if visit[node[0]][node[1]] == False:
            visit[node[0]][node[1]] = True
            cnt = graph[node[0]][node[1]]
            for i in range(8):
                nx = allow[i][0] + node[0]
                ny = allow[i][1] + node[1]
                if 0 <= nx < n and 0 <= ny < n:

                    if visit[nx][ny] == False:

                        graph[nx][ny] = cnt + 1
                        
                        q.append((nx, ny))
            
        if sw == 1:
            return graph[dx][dy]
                        
    return graph[dx][dy]

allow = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

answers = []

tc = int(input())

for i in range(tc):

    n = int(input())

    initialX, initialY = map(int, sys.stdin.readline().split())

    destinationX, destinationY = map(int, sys.stdin.readline().split())

    answers.append(bfs(n, initialX, initialY, destinationX, destinationY))

for i in range(tc):
    print(answers[i])