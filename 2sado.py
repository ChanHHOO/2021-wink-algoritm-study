from itertools import count
import math
from collections import deque

def countOne(binum):
    oneCnt = 0
    for i in range(len(binum)):
        if binum[i] == "1":
            oneCnt += 1
    return oneCnt

def solution(n):
    answer = 0
    binum = bin(n)
    oneCnt = countOne(binum)
    
    while True:
        n += 1
        cBinum = countOne(bin(n))
        if oneCnt == cBinum:
            return n
        
    return 0
print(solution(15))