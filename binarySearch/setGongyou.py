import sys
import math

n, c = map(int, sys.stdin.readline().split())

houses = []

maxHouse = 0

for _ in range(n):

    houses.append(int(sys.stdin.readline()))

houses.sort()

start = 0

end = n - 1

mid = math.ceil((start + end) / 2)

if c >= 4:

    c -= 3

    while c > 0:
        tmpMid = mid
        mid = (start + mid) // 2
        c -= 2

        if c > 0:
            end = tmpMid
    
    print(start, mid, end)
    answer = houses[mid] - houses[start] if houses[mid] - houses[start] < houses[end] - houses[mid] else houses[end] - houses[mid]
    print(answer)
    exit()
elif c == 3:
    answer = houses[mid] - houses[start] if houses[mid] - houses[start] < houses[end] - houses[mid] else houses[end] - houses[mid]
    print(answer)
    exit()
elif c == 2:
    print(end - start)









