import sys
from collections import deque

def dfs(root, removeNode, tree, n):
    
    q = deque()

    q.append(root)

    visit = [False for i in range(n)]


    answer = 0
    while q:
        node = q.popleft()

        if visit[node] == False:
            visit[node] = True
            tmp = tree[node]
            if tmp == []:
                answer += 1
            for i in range(len(tmp)-1, -1, -1):
                if tmp[i] == removeNode:
                    tree[node].pop(i)
                    if tree[node] == []:
                        answer += 1
                    continue
                q.appendleft(tmp[i])
            
    return answer 

n = int(sys.stdin.readline())

tree = {i:[] for i in range(n)}

nums = list(map(int, sys.stdin.readline().split()))

root = 0

for i in range(n):
    if nums[i] == -1:
        root = i
    else:
        tree[nums[i]].append(i)

removeNode = int(sys.stdin.readline())

if root == removeNode:
    print(0)
    exit()
print(dfs(root, removeNode, tree, n))