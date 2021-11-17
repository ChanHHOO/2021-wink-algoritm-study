def solution(prices):
    answer = []
    for i in range(len(prices)):
        sw = 0
        cnt = 0

        if sw != 1:
            for d in range(i ,len(prices)-1):
                cnt += 1
                if prices[i] > prices[d+1]:
                    break
        answer.append(cnt)
    return answer