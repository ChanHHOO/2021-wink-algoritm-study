def solution(progresses, speeds):
    time_spend = []
    answer = []
    for i in range(0, len(progresses)):
        count = 0
        for j in range(progresses[i], 100, speeds[i]):
            count+=1
        time_spend.append(count)
    j_switch = 0
    count = 0
    print(time_spend)
    for i in range(0, len(time_spend)):
        count = 0
        for j in range(j_switch, len(time_spend)):
            if(time_spend[i]>=time_spend[j]):
                count+=1
                j_switch+=1
            else:
                break
        if(count != 0):
            answer.append(count)
                
    return answer