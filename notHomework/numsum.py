#1, 2, 3, 5, 7, 9, 10, 11, 12

#1, 5, 9, 20, 21, 40, 50
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

x = int(sys.stdin.readline())

start = 0

end = n-1

answer = 0

while True:
    
    if end <= start:
        break

    sumVal = nums[start] + nums[end]

    if sumVal == x:

        answer += 1

        start += 1

        end -= 1

    elif sumVal > x:

        end -= 1

    else:

        start += 1
        
print(answer)
