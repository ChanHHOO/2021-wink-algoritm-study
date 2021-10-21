import sys

n, m = map(int, sys.stdin.readline().split(" "))

tree = {}

for i in range(m):

    a, b = map(int, sys.stdin.readline().split(" "))
    try:
        tree[a].append(b)
    except:
        tree[a] = [b]
    try:
        tree[b].append(a)
    except:
        tree[b] = [a]

q = [1]
visit = [False for _ in range(n)]
qq =[False for _ in range(n)]
l = 0
tmp = []
answer = []
qq[0] = True
while q:
    node = q.pop(0)

    if visit[node-1] == False:

        visit[node-1] = True

        for child in tree[node]:
            if qq[child-1] == False:
                qq[child-1] = True
                q.append(child)
        
        tmp.append(node)

        if l != 0:
            l -= 1
        else:
            
            answer.append(tmp)
            tmp = []
            l = len(q)-1
print(min(answer[-1]), len(answer)-1, len(answer[-1]))
