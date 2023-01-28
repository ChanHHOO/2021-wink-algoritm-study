import sys



def solution(cost, x):
    paintLen = len(cost)

    arr = [[0] * (x + 1) for _ in range(paintLen)]

    for i in range(x + 1):
        if i >= cost[0]:
            arr[0][i] =  cost[0]
    
    for i in range(1, paintLen):

        for j in range(x + 1):

            cnt = j // cost[i]
            
            # while(cnt >= 0):
            #     a = (2**i) * cnt
            #     b = arr[i][j - cost[i]*cnt]
            #     arr[i][j] = max(arr[i][j], a + b)
            #     cnt -= 1
            sum = 0
            if j >= cost[i]:
                sum = arr[i-1][j - cost[i]] + (2**i)
            arr[i][j] = sum
            # arr[i][j] = max(arr[i][j], arr[i-1][j])
    # print(arr)
    return (arr[-1][-1])



    

if __name__ == '__main__':
    solution([3, 4, 1], 8)