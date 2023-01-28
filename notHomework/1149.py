import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split(" "))) for _ in range(n)]

dp = [[graph[0][0], graph[0][1], graph[0][2]]]

for i in range(1, n):
    dp.append([0,0,0])
    dp[i][0] = graph[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = graph[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = graph[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))