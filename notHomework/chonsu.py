import sys
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split(" "))
m = int(sys.stdin.readline())
tree = {}

for i in range(m):

    x, y = map(int, sys.stdin.readline().split(" "))

    try:
        tree[x].append(y)

    except:
        tree[x] = [y]
    
    try:
        tree[y].append(x)
    except:
        tree[y] = [x]



stack = []
stack.append(sorted(tree.keys())[0])
visited = []
fam = []
while stack:
    node = stack.pop(0)
    if node not in visited:
        visited.append(node)
        if n in tree[node]:
            fam = tree[node]
            
        for i in reversed(tree[node]):
            stack.insert(0, i)
try:
    answer = 1 if a in fam and b in fam else abs(visited.index(a) - visited.index(b))
except:
    answer = -1
    
print(answer)