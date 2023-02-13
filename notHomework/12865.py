import sys

input = sys.stdin.readline

n, k = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(n)]

items.sort(key=lambda x:x[1])

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = items[i-1]
    for j in range(1, k+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])