from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

tree = {i:[] for i in range(1, n+1)}


for i in range(m):
    a, b= map(int, sys.stdin.readline().split())
    tree[b].append(a)
    
q = deque()
answers = []
maxVal = 0

for start in range(1, n+1):
    q.append(start)
    visit = [False for _ in range(n+1)]
    visit[start] = True
    cnt = 0

    while q:
        node = q.pop()
        visit[node] = True
        for next in tree[node]:
            if visit[next] == False:
                cnt += 1
                
                q.append(next)
    # print(cnt)
    if cnt > maxVal:
        maxVal = cnt
        answers = [start]
    elif cnt == maxVal:
        answers.append(start)

answers.sort()
for i in range(len(answers)-1):
    print(answers[i], "", end="")
print(answers[len(answers) - 1])
    



