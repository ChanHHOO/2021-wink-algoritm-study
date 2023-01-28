import sys
from collections import deque

tc = int(input())

for _ in range(tc):
    answer = 1
    n, target = map(int, sys.stdin.readline().split())

    priority = deque(list(map(int, sys.stdin.readline().split())))

    for i in range(n):

        priority[i] = [i, priority[i]]
    
    while True:

        for i in range(1, len(priority)):
            if priority[0][1] < priority[i][1]:
                priority.append(priority.popleft())
                break
        else:
            if target == priority[0][0]:
                break
            priority.popleft()
            
            answer += 1
    print(answer)