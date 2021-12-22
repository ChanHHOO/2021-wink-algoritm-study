import sys
import time 
n, m = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split(" "))))

allows = [(-1,0), (0, 1), (1, 0), (0, -1)]

allowCnt = 3 if d - 1 == -1 else d - 1

i = r 

j = c

if graph[i][j] == 0 : graph[i][j] = 2
isBack = False
print("==========")
answer = 0
while True:

    isClean = False

    walls = 0

    cleanAreas = 0
    
    for k in range(4):

        # time.sleep(0.5)

        i += allows[allowCnt][0]

        j += allows[allowCnt][1]

        if isBack == True:
            
            if allowCnt == 0:allowCnt = 2        
            elif allowCnt == 2:allowCnt = 0
            elif allowCnt == 1:allowCnt = 3
            elif allowCnt == 3:allowCnt = 1
            allowCnt = 3 if allowCnt - 1 == -1 else allowCnt - 1
            i += allows[allowCnt][0]

            j += allows[allowCnt][1]


        if 0 <= i < n and 0 <= j < m:
            
            if graph[i][j] == 0:
                print(i, j, allowCnt)
                graph[i][j] = 2

                answer += 1

                allowCnt = 3 if allowCnt - 1 == -1 else allowCnt - 1

                break

            elif graph[i][j] == 1: walls += 1    

            else : cleanAreas += 1
        print(i, j)
        i -= allows[allowCnt][0]

        j -= allows[allowCnt][1]
        
        allowCnt = 3 if allowCnt - 1 == -1 else allowCnt - 1
        isBack = False

        

    else:
        

        print(i, j, allowCnt ,"=-=")
        allowCnt = 0 if allowCnt + 1 == 4 else allowCnt + 1

        if walls == 4 or graph[i + (allows[allowCnt][0] * -1)][j + (allows[allowCnt][0] * -1)] == 1:
            break
        if allowCnt == 0:allowCnt = 2        
        elif allowCnt == 2:allowCnt = 0
        elif allowCnt == 1:allowCnt = 3
        elif allowCnt == 3:allowCnt = 1

        isBack = True
        print(allowCnt)
        

print(answer)





