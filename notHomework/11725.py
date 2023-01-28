import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visit = [False] * (n + 1)
    while q:
        node = q.popleft()
        if not visit[node]:
            visit[node] = True
            tmp = graph[node]
            for nextNode in tmp:
                if answer[nextNode] == 0:
                    answer[nextNode] = node
                    q.append(nextNode)
    for ans in answer[2:]:
        print(ans)


input = sys.stdin.readline

n = int(input())

graph = {i : [] for i in range(1, n+1)}

answer = [0] * (n+1)

answer[1] = 1

for i in range(n-1):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

bfs(1)