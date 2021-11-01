import sys

n, m = map(int, input().split(" ")) 

graph = {}

answer = 0

for i in range(1, n+1):
    graph[i] = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)

visit = [False for _ in range(n)]

isQ = [False for _ in range(n)]

if m != 0:
    while graph:

        currentGraphKeys = list(graph.keys())

        q = [currentGraphKeys[0]]

        while q:

            node = q.pop(0)
            
            if visit[node-1] == False:
                visit[node-1] = True
                
                for item in graph[node]:
                    if visit[item-1] == False and isQ[item-1] == False:
                        isQ[item-1] = True
                        q.append(item)
                graph.pop(node)
        answer += 1
else:
    answer = n
print(answer)