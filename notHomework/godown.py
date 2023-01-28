import sys

input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):

    tmp = list(map(int, input().split(" ")))

    graph.append(tmp)

min_old = [i for i in graph[0]]
max_old = [i for i in graph[0]]
min_new = [0]*3
max_new = [0]*3

for i in range(1, n):

    min_new[0] = min(min_old[0], min_old[1]) + graph[i][0]
    min_new[1] = min(min_old[0], min_old[1], min_old[2]) + graph[i][1]
    min_new[2] = min(min_old[1], min_old[2]) + graph[i][2]

    max_new[0] = max(max_old[0], max_old[1]) + graph[i][0]
    max_new[1] = max(max_old[0], max_old[1], max_old[2]) + graph[i][1]
    max_new[2] = max(max_old[1], max_old[2]) + graph[i][2]

    min_old = [i for i in min_new]
    max_old = [i for i in max_new]

print(max(max_old), min(min_old))