import sys

input = sys.stdin.readline

tc = int(input())

while tc:

    n = int(input())

    graph = []

    for i in range(2):
        
        graph.append(list(map(int, input().split(" "))))
        graph[i].insert(0, 0)

    dp = [[0, graph[0][1]], [0, graph[1][1]]]

    for i in range(2, n+1):
        dp[0].append(max(dp[1][i-2], dp[1][i-1]) + graph[0][i])
        dp[1].append(max(dp[0][i-2], dp[0][i-1]) + graph[1][i])
    print(max(dp[0][-1], dp[1][-1]))
    

    tc -= 1