def solution(priorities, location):
    answer = 0
    indexs = [ x for x in range(1, len(priorities)+1)]
    cnt = 0
    
    while(True):
        
        if((max(priorities) == priorities[0]) and  (len(priorities) != 0)):
            print(priorities, indexs , answer)
            answer += 1
            if(location == indexs[0]-1):
                break
            priorities[0] = 0
            indexs[0] = 0
        else:
            priorities.append(priorities[0])
            indexs.append(indexs[0])
            del priorities[0]
            del indexs[0]
        
    return answer