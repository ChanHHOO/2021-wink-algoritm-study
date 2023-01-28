from itertools import combinations
import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = []

homes = []

chickens = []

for i in range(n):
    tmp = list(map(int, input().split(" ")))
    for j in range(n):
        if tmp[j] == 1:
            homes.append((i, j))
        elif tmp[j] == 2:
            chickens.append((i, j))
    graph.append(tmp)
result = 9999919239912
for chi in combinations(chickens, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in homes: 
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)
print(result)