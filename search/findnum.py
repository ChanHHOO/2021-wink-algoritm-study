import sys

n = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
numList.sort()

m = int(sys.stdin.readline())
targetList = list(map(int, sys.stdin.readline().split()))
answers = []
for target in targetList:
    low = 0
    high = n - 1
    isFind = False
    while(low <= high):
        mid = (low + high) // 2
        # print(low, high)
        if numList[mid] == target:
            isFind = True
            break
        elif numList[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    print(int(isFind))
# 5
# 4 1 5 2 3
# 1
# 9