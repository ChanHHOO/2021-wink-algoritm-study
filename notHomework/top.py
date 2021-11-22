import sys
from collections import deque

n = int(sys.stdin.readline())
towers = deque(map(int, sys.stdin.readline().split(" ")))
answers = [0]
stack = deque()
stack.append((towers.popleft(), 0))
for i in range(1, n):
    target = towers.popleft()
    position = 0
    if stack[-1][0] <= target:
        for j in range(len(stack)):
            stack.pop()
            if len(stack) != 0 and stack[-1][0] > target:
                position = stack[-1][1] + 1
                break
        stack.append((target, i))
        answers.append(position)
    else:
        stack.append((target, i))
        answers.append(stack[-1][1])

for i in range(n):
    print(answers[i], end=" ")
