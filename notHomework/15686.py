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
result = math.inf
for chi in combinations(chickens, m):  # m개의 치킨집 선택
    
    cityDis = 0
    for home in homes:
        chickDis = math.inf
        for store in chi:
            tmp = abs(home[0] - store[0]) + abs(home[1] - store[1])
            if chickDis > tmp:
                chickDis = tmp
        cityDis += chickDis
    
    if result > cityDis:
        result = cityDis
print(result)