from collections import deque
import sys
# def bfs(graph, a, b, n):
#     visit = [False for _ in range(1, n+1)]
#     q = deque()
#     q.append(a)
#     while q:
#         print(q)
#         node = q.pop()
#         if visit[node - 1] == False:
#             visit[node-1] = True
#             q.extend(graph[node])


# n = int(sys.stdin.readline())

# a, b = map(int, sys.stdin.readline().split(" "))

# m = int(sys.stdin.readline())

# graph = {}

# for i in range(1, n+1):
#     graph[i] = []

# for i in range(m):
#     x, y = map(int, sys.stdin.readline().split(" "))

#     graph[x].append(y)
#     graph[y].append(x)
# bfs(graph, a, b, n)

global isAns
isAns = False
def dfs(graph, current, to, visit, answer):
    visit[current] = True
    global isAns
    if current == to:
        print(answer)
        isAns = True
        return answer
    for next in graph[current]:
        if visit[next] == False:
            dfs(graph, next, to, visit, answer+1)
                

input = sys.stdin.readline

n = int(input())

fr, to = map(int, input().split(" "))

m = int(input())

graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

visit = [False for _ in range(n+1)]

a = dfs(graph, fr, to, visit, 0)
if not isAns:
    print(-1)