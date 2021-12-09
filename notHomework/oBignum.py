import sys
from collections import deque


n = int(sys.stdin.readline())

nums = deque(map(int, sys.stdin.readline().split()))

stack = [[nums.popleft(), 0]]

answer = []

for i in range(len(nums)):
    
    num = nums.popleft()

    for j in range(len(stack)):

        if stack[-1][0] >= num:
            
            break

        else:
            answer.append((num, stack[-1][1]))
            stack.pop()

            

    stack.append([num, i+1])


for i in range(len(stack)):
    answer.append((-1, stack[i][-1]))

answer.sort(key=lambda x : x[1])

ansStr = ""

for i in answer:

    ansStr += (str(i[0]) + " ")

print(ansStr)