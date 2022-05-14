import sys
from collections import deque

tc = int(sys.stdin.readline())
answers = []
for _ in range(tc):

    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    nums.sort()

    nums = deque(nums)

    answer = [0 for _ in range(n)]

    for i in range(n//2):

        answer[i] = nums.popleft()

        answer[n-1-i] = nums.popleft()

    if n % 2 == 1:
        answer[n//2] = nums.pop()

    maxVal = 0

    for i in range(n-1):
        if maxVal <= abs(answer[i] - answer[i+1]):
            maxVal = abs(answer[i] - answer[i+1])
    if maxVal <= abs(answer[-1] - answer[0]):
        maxVal = abs(answer[-1] - answer[0])
    answers.append(maxVal)
for answer in answers:
    print(answer)

