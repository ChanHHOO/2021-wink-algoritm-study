import sys

from collections import deque

n = int(sys.stdin.readline())

graph = list(map(int, input().split()))

dp = [0 for _ in range(n)]

if graph[0] or n == 1:
    dp[0] = 1

for i in range(n):
    if dp[i] != 0:
        for j in range(i+1, i+graph[i]+1):            

            if j < n:

                if dp[j] == 0:
                    
                    dp[j] = dp[i] + 1

                else:

                    dp[j] = min(dp[j], dp[i] + 1)

print(dp[-1]-1 if dp[-1] else -1)