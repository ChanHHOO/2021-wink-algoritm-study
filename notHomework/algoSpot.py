import math
import sys
import heapq
from collections import deque

allow = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dijkstra(graph, dist, visit):
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    dist[0][0] = 0
    cnt = 0

    while pq:
        cnt += 1
        
        current_dist, currentY, currentX = heapq.heappop(pq)

        if current_dist > dist[currentY][currentX]:
            continue
        if currentY == m - 1 and currentX == n - 1:
            print(current_dist)
            break
        for i in range(4):
            nx = currentX + allow[i][1]
            ny = currentY + allow[i][0]

            # if ny < 0 or ny >= m or nx < 0 or nx >= n:
                
            if 0 <= ny < m and 0 <= nx < n:  # 범위를 벗어나거나 이미 방문했으면 진행x
                if current_dist + graph[ny][nx] < dist[ny][nx]:
                    dist[ny][nx] = current_dist + graph[ny][nx]
                    heapq.heappush(pq, (dist[ny][nx], ny, nx))
    print(cnt)

input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = []

for i in range(1, m+1):

    tmp = input()

    tmpList = list(map(int, tmp[:-1]))

    graph.append(tmpList)
visit = [[False] * n for _ in range(m)]
dist = [[math.inf] * n for _ in range(m)]
dijkstra(graph, dist, visit)

# import heapq

# M, N = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# distance = [[1e10] * M for _ in range(N)]
# print(arr)

# dr = [-1, 0, 1, 0]  # 상 우 하 좌
# dc = [0, 1, 0, -1]  # 상 우 하 좌


# def dijkstra():
#     q = []
#     heapq.heappush(q, (0, 0, 0))
#     distance[0][0] = 0
#     while q:
#         cost, r, c = heapq.heappop(q)

#         if cost > distance[r][c]:
#             continue

#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]

#             if nr < 0 or nr >= N or nc < 0 or nc >= M:  # 범위를 벗어나거나 이미 방문했으면 진행x
#                 continue

#             if cost + arr[nr][nc] < distance[nr][nc]:
#                 distance[nr][nc] = cost + arr[nr][nc]
#                 heapq.heappush(q, (distance[nr][nc], nr, nc))


# dijkstra()
# print(distance[N - 1][M - 1])