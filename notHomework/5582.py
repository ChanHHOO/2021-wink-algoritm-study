import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

maxVal = 0
dp = [[0]*len(str2) for _ in range(len(str1))]

for i in range(len(str1)):

    for j in range(len(str2)):

        if str1[i] == str2[j]:

            if j != 0 and i != 0:

                dp[i][j] = dp[i-1][j-1] + 1
            
            else:
                dp[i][j] = 1
            maxVal = maxVal if maxVal > dp[i][j] else dp[i][j]
print(maxVal)



