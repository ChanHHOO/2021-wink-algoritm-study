def solution():
    n = int(input())
    um = []
    yang = []
    isZero = False
    oneCnt = 0
    answer = 0
    for _ in range(n):
        tmp = int(input())
        if tmp == 1:
            oneCnt += 1
        elif tmp > 0:
            yang.append(tmp)
        elif tmp < 0:
            um.append(tmp)
        else:

            
            isZero = True
    yang = sorted(yang, reverse=True)
    um = sorted(um)

    for _ in range(len(yang)//2):
        answer += (yang.pop(0) * yang.pop(0))
    for _ in range(len(um)//2):
        answer += (um.pop(0) * um.pop(0))
    
    if isZero:
        print(answer + sum(yang) + oneCnt)
    else:
        print(answer + sum(um) + sum(yang) + oneCnt)

solution()