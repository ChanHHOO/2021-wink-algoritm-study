import sys

def solution(box):
    # Write your code here
    newList = []
    for i in range(len(box)):
        newList.append((box[i], i))
    newList.sort(key=lambda x : x[0])
    l = len(box)
    while True:
        i = 0
        j = l - 1
        for _ in range(l /2):
            if newList[i][0] < newList[j][0] and newList[i][1] < newList[j][1]:
                newList[i][0] += 1
                newList[j][0] -= 1
                i += 1
                j -= 1
                while True:
                    if 


        
    return max(box)



solution([5, 15, 19])