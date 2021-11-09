import sys
n, k = map(int, input().split(" "))

bags = []

for i in range(n):
    a, b = map(int, input().split(" "))
    bags.append((a, b))

dp = []
idxs = [[i] for i in range(n)]
for i in range(n):
    tmp = []
    for j in range(i+1, len(bags)):
        if i not in idxs[j] and bags[i][0]+bags[j][0] <= k:
            tmp.append((bags[i][0]+bags[j][0], bags[i][1] + bags[j][1]))
            idxs.append([i] + idxs[j])
            
    bags += tmp
bags.sort(key=lambda x:x[1])
print(bags[-1][1])
