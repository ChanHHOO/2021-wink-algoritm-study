import sys
from collections import deque
import math
n, k = map(int, sys.stdin.readline().split())

distances = [math.inf for _ in range(100001)]

distances[n] = 0

q = deque()

q.append(n)

visit = [False for _ in range(100001)]

while distances[k] == math.inf:
    
    node = q.popleft()

    if visit[node] == False:
        
        visit[node] = True
        if node - 1 < 100001 and visit[node - 1] == False:
            distances[node-1] = min(distances[node-1], distances[node] + 1)
            q.append(node-1)
        if node + 1 < 100001 and visit[node + 1] == False:
            distances[node+1] = min(distances[node+1], distances[node] + 1)
            q.append(node+1)
        if node * 2 < 100001 and visit[node * 2] == False:
            distances[node * 2] = min(distances[node*2], distances[node])
            q.appendleft(node*2)

print(distances[k])