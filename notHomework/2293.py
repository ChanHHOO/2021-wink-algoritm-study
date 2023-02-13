import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0]*(k+1)

for i in range(1, n+1):
    coin = coins[i-1]
    for j in range(1, k+1):

        if j == coin:
            dp[j] = dp[j] + 1
        elif j > coin:
            dp[j] = dp[j] + dp[j-coin]
        else:
            dp[j] = dp[j]
print(dp[-1])