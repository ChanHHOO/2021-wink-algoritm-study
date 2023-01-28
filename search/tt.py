from collections import deque
import sys

n = int(sys.stdin.readline())

tree = {i:[] for i in range(1, n+1)}

for i in range(1, n+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(0, n):
        if tmp[j] == 1:
            tree[i].append(j+1)
    tree[i].sort()

q = deque()

graph = [[0 for _ in range(n)]for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sw = 0
        q.append(i)
        visit = [0 for _ in range(n+1)]
        isOne = False
        while q:
                
            node = q.popleft()
            if visit[node] == 1 and node == i:
                graph[i-1][i-1] += 1
            if visit[node] == 0:
                visit[node] += 1
                if node == j:
                    sw = 1
                    graph[i-1][j-1] = 1
                q.extend(tree[node])
# print(graph)
for i in range(n):
    for j in range(n):
        if i == j and graph[i][j] >= 2:
            print(1,"", end='')
        elif i != j and graph[i][j] >= 1:
            print(1,"",  end='')
        else:
            print(0,"",  end='')
    print()


'''
3
0 1 0
0 0 1
1 0 0
'''