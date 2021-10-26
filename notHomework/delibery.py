import math
def solution(N, road, K):
    answer = 1
    graph = [[math.inf for _ in range(N)] for _ in range(N)]
    for i in range(len(road)):
        if graph[road[i][0] - 1][road[i][1] - 1] > road[i][2]:
            graph[road[i][0] - 1][road[i][1] - 1] = road[i][2]
            graph[road[i][1] - 1][road[i][0] - 1] = road[i][2]

    distance = graph[0][::]
    visit = [False for _ in range(N)]
    
    for i in range(1, N):
        minVal = math.inf
        minidx = 0
        for j in range(1, N):
            if visit[j] == False and minVal > distance[j]:
                minidx = j
                minVal = distance[j]
        visit[minidx] = True
        for j in range(1, N):
            if j != minidx:
                distance[j] = min(distance[j], distance[minidx]+graph[minidx][j])

    for i in range(1, N):
        if distance[i] <= K: answer += 1
    return answer

solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	, 4)