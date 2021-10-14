def solution(weights, head2head):
    answer = []
    winPercents = []
    for i in range(len(head2head)):
        winPercent = head2head[i].count("W") / (len(head2head)-1)
        biggerWin = 0
        for j in range(head2head[i].count("W")):
            if weights[i] < weights[head2head[i].index("W")]:

                biggerWin += 1

                head2head[i] = head2head[i][:head2head[i].index("W")] + "-" + head2head[i][head2head[i].index("W")+1:]
                
        winPercents.append([winPercent, biggerWin, weights[i], i+1])
    print(winPercents)
    for i in range(len(head2head)):
        for j in range(len(head2head)-1):
            if winPercents[j][0] < winPercents[j+1][0]:
                winPercents[j], winPercents[j+1] = winPercents[j+1], winPercents[j]
            elif winPercents[j][0] == winPercents[j+1][0]:
                if winPercents[j][1] < winPercents[j+1][1]:
                    winPercents[j], winPercents[j+1] = winPercents[j+1], winPercents[j]
                elif winPercents[j][1] == winPercents[j+1][1]:
                    if winPercents[j][2] < winPercents[j+1][2]:
                        winPercents[j], winPercents[j+1] = winPercents[j+1], winPercents[j]
                    elif winPercents[j][3] == winPercents[j+1][3]:
                        winPercents[j], winPercents[j+1] = winPercents[j+1], winPercents[j]
    for i in range(len(weights)):answer.append(winPercents[i][3])
    return answer

solution([145,92,86],["NLW","WNL","LWN"]	)