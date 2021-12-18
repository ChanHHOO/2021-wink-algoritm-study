import math
from collections import deque

def solution(n, edge):
    answer = 0

    distances = [math.inf for _ in range(n + 1)]

    visit = [False for _ in range(n+1)]

    distances[1] = 0

    graph = {i : [] for i in range(1, n+1)}

    for i in range(len(edge)):

        graph[edge[i][0]].append(edge[i][1])

        graph[edge[i][1]].append(edge[i][0])

    q = deque()

    q.append(1)

    while q:
        node = q.popleft()

        distance = distances[node]

        if visit[node] == False:

            visit[node] = True

            for i in range(len(graph[node])):

                distances[graph[node][i]] = min(distances[graph[node][i]], distance + 1)

                q.append(graph[node][i])
    

    maxVal = max(distances[1:])
    return distances.count(maxVal)



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))