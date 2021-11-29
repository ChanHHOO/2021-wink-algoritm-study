import sys
from collections import deque

allow = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n = int(sys.stdin.readline())

graph = []

nums = set()

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    nums.update(tmp)
    graph.append(tmp)


def dfs(ci, cj, visit):
    
    stack = deque()
    stack.append((ci, cj))
    while stack:
        node = stack.popleft()
        if visit[node[0]][node[1]] == False:
            visit[node[0]][node[1]] = True
            for i in range(4):
                if 0 <= node[0] + allow[i][0] < n and 0 <= node[1] + allow[i][1] < n:
                    stack.append((node[0] + allow[i][0], node[1] + allow[i][1]))

nums = list(nums)
nums.append(0)
answers = []
for k in range(len(nums)):
    visit = [[False] * n for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= nums[k]:
                visit[i][j] = True

    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                dfs(i, j, visit)
                answer += 1
    answers.append(answer)
print(max(answers))
