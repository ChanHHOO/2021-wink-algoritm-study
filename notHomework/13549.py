import sys
from collections import deque
import math

n, k = map(int, sys.stdin.readline().split())

visit = [math.inf for _ in range(1000000)]

positions = deque()

positions.append((n, 0))

if n != k:        
    while positions:
            # print(positions)
            # print()
        current_pos, current_time = positions.popleft()
        jump_pos, jump_time = current_pos * 2, current_time
        if jump_pos < 200001:
            if visit[jump_pos] > jump_time:
                visit[jump_pos] = jump_time
                positions.append((jump_pos, jump_time))

        go, back = current_pos + 1, current_pos - 1
        go_time, back_time = current_time + 1, current_time + 1
            
        if go < 200001:
            if visit[go] > go_time:
                visit[go] = go_time
                positions.append((go, go_time))
        if 0 <= back < 200001:
            if visit[back] > back_time:
                visit[back] = back_time
                positions.append((back, back_time))

else:
    print(0)
    exit()
print(visit[k])