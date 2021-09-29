def solution():
    cnt = int(input())
    building = list(map(int, input().split(" ")))
    answer = 0
    answers = []
    for i in range(cnt):
        minGi = 9999
        answer = 0
        #좌
        if i != 0:
            for j in range(i-1, 0, -1):
                if building[i] != building[j]:
                    gi = abs(building[i] - building[j]) / abs((i+1) - (j+1))
                else:
                    gi = 0
                minGi = min(minGi, gi)
                if gi == minGi:
                    answer += 1
            minGi = 9999
        # #우
        
        for j in range(i+1, cnt):
            if building[i] != building[j]:
                gi = abs(building[i] - building[j]) / abs((i+1) - (j+1))
            else:
                gi = 0
            minGi = min(minGi, gi)
            
            if i == 0:
                print(gi)
                print(minGi)
            if gi == minGi:
                answer += 1
        
        answers.append(answer)
    print(answers)
solution()