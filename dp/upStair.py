from curses.ascii import FS
import sys
n = int(sys.stdin.readline())

stairs = [(1, int(sys.stdin.readline())) for _ in range(n)]
stairs.append((0,0))
stairs.append((0,0))
dp = [(0, 0) for _ in range(n+2)]

dp[0] = stairs[0]
if n >= 2:
    dp[1] = (2, stairs[0][1] + stairs[1][1])

    for i in range(n-2):
        fStep = (dp[i][0] + stairs[i+1][0], dp[i][1] + stairs[i+1][1])
        sStep = (1, dp[i][1] + stairs[i+2][1])
        if fStep[0] < 3 and dp[i-1][1] + stairs[i+1][1] + stairs[i+2][1] < fStep[1] + stairs[i+3][1]:
            dp[i+1] = fStep

        dp[i+2] = sStep
    print(stairs)
    print(dp)

else:
    print(stairs[0][1])