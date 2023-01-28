import sys
from collections import deque


def isComplate(n, startI, startJ, square):
    color = square[startI][startJ]
    for i in range(startI, n+startI):
        for j in range(startJ, n+startJ):
            if square[i][j] != color:
                return -1
    return color


def squareRec(n, square, i, j, answers):
    
    if n == 1:
        answers[square[i][j]] += 1
        return
    else:
        color = isComplate(n, i, j, square)
        if color != -1:
            answers[color] += 1
            return
        else:
            n //= 2
            squareRec(n, square, i, j + n, answers)
            squareRec(n, square, i, j, answers)
            squareRec(n, square, i + n, j, answers)
            squareRec(n, square, i + n, j + n, answers)
        return


n = int(sys.stdin.readline())

square = []

for i in range(n):
    square.append(list(map(int, sys.stdin.readline().split())))
answers = [0, 0]
squareRec(n, square, 0, 0, answers)
print(answers[0])
print(answers[1])