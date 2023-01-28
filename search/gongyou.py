import sys
import math

def findMiddle(arr, low, high, mid):
    gn = 0
    cha = 0
    for i in range(low, high):
        s = arr[i] - arr[i-1] + abs(arr[i] - arr[i+1])
        if s > cha:
            cha = s
            gn = i
    return (gn, cha)

def bin(c, low, high, gong, arr):
    if(c <= 0):
        return
    else:
        (mid, midCha) = findMiddle(arr, low+1, high-1, (arr[low] + arr[high]) / 2)
        gong.append(arr[mid])
        (left, leftCha) = findMiddle(arr, low + 1, mid - 1, (arr[low] + arr[mid]) / 2)
        (right, rightCha) = findMiddle(arr, mid + 1, high - 1, (arr[mid] + arr[high]) / 2)
        print(low, high, mid, leftCha, rightCha)
        if leftCha > rightCha:
            bin(c - 1, low, mid, gong, arr)
            c -= 1
            bin(c - 1, mid, high, gong, arr)
        else:
            bin(c - 1, mid, high, gong, arr)
            c -= 1
            bin(c - 1, low, mid, gong, arr)


n, c = map(int, sys.stdin.readline().split())
c -= 2

arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

gong = [min(arr)]

bin(c, 0, n-1, gong, arr)

gong.append(max(arr))

print(gong)




