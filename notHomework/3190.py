import sys
from collections import deque

allows = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def getNextAllow(current_arrow, command):
    nextAllow = None
    if current_arrow == 0:
        if command == 'L': nextAllow = 3
        else: nextAllow = 1
    elif current_arrow == 1:
        if command == 'L': nextAllow = 0
        else: nextAllow = 2
    elif current_arrow == 2:
        if command == 'L': nextAllow = 1
        else: nextAllow = 3
    else:
        if command == 'L': nextAllow = 2
        else: nextAllow = 0
    return nextAllow
            

q = deque()

input = sys.stdin.readline

n = int(input())

apple_cnt = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(apple_cnt):
    a, b = map(int, input().split())
    graph[a][b] = 1

command_cnt = int(input())
commands = {}
for _ in range(command_cnt):
    time, command = input().split()
    commands[int(time)] = command
q.append((1, 1))
allow = 1
time = 1
for _ in range(1, 10001):

    # print(q, time, allow)
    # a = input()
    ny = q[-1][0] + allows[allow][0]
    nx = q[-1][1] + allows[allow][1]
    if 0 < ny <= n and 0 < nx <= n and (ny, nx) not in q:
        q.append(( q[-1][0] + allows[allow][0], q[-1][1] + allows[allow][1] ))
    else: break
    
    if graph[q[-1][0]][q[-1][1]]:
        graph[q[-1][0]][q[-1][1]] = 0
    else:
        q.popleft()

    try:
        allow = getNextAllow(allow, commands[time])
    except:
        pass
    time += 1

print(time)

