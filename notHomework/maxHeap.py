import sys
import heapq

heap = []

n = int(sys.stdin.readline())

for i in range(n):

    c = int(sys.stdin.readline())

    if c == 0:
        if heap:
            tmp = heapq.heappop(heap)
            print(tmp[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-c, c))