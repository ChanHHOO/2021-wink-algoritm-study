import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

sums = [[0] * n for _ in range(n)]

graph = []

for i in range(n):
    tmp = list(map(int, input().split(" ")))
    
    graph.append(tmp)
    for j in range(n):
        if i == 0 and j == 0:
            sums[i][j] = tmp[0]
        elif i == 0:
            sums[i][j] = sums[i][j-1] + tmp[j]
        elif j == 0:
            sums[i][j] = tmp[0] + sums[i-1][j]
        else:
            sums[i][j] = sums[i][j-1] + sums[i-1][j] + tmp[j] - sums[i-1][j-1]
print(sums)


answer = []
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split(" "))
    x1 -= 1; y1 -= 1; x2 -=1; y2 -= 1
    ans, top, left, dup = 0, 0, 0, 0

    if x1-1 >= 0:
        top = sums[x1-1][y2]
    if y1-1 >= 0:
        left = sums[x2][y1-1]
    if top and left:
        dup = sums[x1-1][y1-1]

    print(sums[x2][y2] - top - left + dup)
    