import heapq
import sys

input = sys.stdin.readline

tc = int(input())

while(tc):

    max_q = []
    min_q = []
    valid_dict = {}

    n = int(input())
    for i in range(n):
        command, num = input().split(" ")
        num = int(num)
        
        if command == "I":
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, num * -1)
            try:
                valid_dict[num] += 1
            except:
                valid_dict[num] = 1
        else:
            try:
                if num == -1 and min_q:
                    target = heapq.heappop(min_q)
                    while not valid_dict[target]:
                        target = heapq.heappop(min_q)
                    valid_dict[target] -= 1
                elif num == 1 and max_q:
                    target = heapq.heappop(max_q) * -1
                    while not valid_dict[target]:
                        target = heapq.heappop(min_q) * -1
                    valid_dict[target] -= 1
            except:
                continue
    tc -= 1

    minVal = 0
    while min_q:
        minVal = heapq.heappop(min_q)
        if valid_dict[minVal]:
            break
    else:
        minVal = 0
    maxVal = 0
    while max_q:
        maxVal = heapq.heappop(max_q) * -1
        if valid_dict[maxVal]:
            break
    else:
        maxVal = 0
    if maxVal == 0 and minVal == 0:
        print("EMPTY")
    else:
        print(maxVal if maxVal!=0 else minVal, minVal if minVal != 0 else maxVal)