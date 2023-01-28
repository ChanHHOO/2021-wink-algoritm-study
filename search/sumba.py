"""
0 0 3 2 1 2 0 3 0 2 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0
q : 6, 10, 3, 8
q 에는 target 보다 작은 수만 들어감
"""
import sys
import math
from collections import deque
n, m = map(int, sys.stdin.readline().split())

jido = [math.inf for _ in range(100002)]
jido[n] = 0
q = deque([n])

while q:
    x = q.popleft()
    
    if x - 1 >= 0 and jido[x-1] > jido[x] + 1:
        jido[x-1] = jido[x] + 1
        q.append(x-1)
    if x + 1 <= 100001 and jido[x+1] > jido[x] + 1:
        jido[x+1] = jido[x] + 1
        q.append(x+1)
    if x * 2 <= 100001 and jido[x*2] > jido[x] + 1:
        jido[x*2] = jido[x] + 1
        q.append(x*2)
    # if x == m:
    #     break
print(jido[m])
