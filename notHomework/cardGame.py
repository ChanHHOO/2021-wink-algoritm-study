import heapq
import sys
hq = []

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    heapq.heappush(hq, nums[i])

for i in range(m):
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)

    heapq.heappush(hq, a+b)
    heapq.heappush(hq, a+b)

print(sum(hq))