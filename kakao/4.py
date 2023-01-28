def solution(cost, x):
    paintLen = len(cost)

    arr = [[0] * (x + 1) for _ in range(paintLen)]

    for i in range(x + 1):
        if i >= cost[0]:
            arr[0][i] =  (2**0) * (i // cost[0])
    for i in range(1, paintLen):

        for j in range(x + 1):

            cnt = j // cost[i]
            
            while(cnt >= 0):
                a = (2**i) * cnt
                b = arr[i][j - cost[i]*cnt]
                arr[i][j] = max(arr[i][j], a + b)
                cnt -= 1
            arr[i][j] = max(arr[i][j], arr[i-1][j])
            
    return (arr[-1][-1])
