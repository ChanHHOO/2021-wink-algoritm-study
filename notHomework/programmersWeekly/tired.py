import itertools

def solution(k, dungeons):
    answer = 0
    indexs = [str(i) for i in range(len(dungeons))]
    indexs = list(map(''.join, itertools.permutations(indexs)))
    for i in range(len(indexs)):
        cnt = 0
        kk = k
        for j in range(len(indexs[i])):
            if kk >= dungeons[int(indexs[i][j])][0]:
                cnt += 1    
                kk -=  dungeons[int(indexs[i][j])][1]
            else:
                break
        if cnt >= answer:
            answer = cnt
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]	))