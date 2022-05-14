import sys
from collections import deque

tc = int(sys.stdin.readline())
answer = []
for _ in range(tc):

    command = sys.stdin.readline()

    n = int(sys.stdin.readline())

    nums = sys.stdin.readline()

    nums = deque(nums[1:-2].split(","))
    sw = 0
    if n:
        for i in range(len(command)):
            if command[i] == "R":
                nums.reverse()
            elif command[i] == "D":
                if nums:
                    nums.popleft()
                else:
                    sw = 1
                    break
    else:
        if "D" in command:
            answer.append("error")
            break

    if sw == 1:
        answer.append("error")
        continue

    answer.append("["+",".join(nums)+"]")

for i in range(tc):

    print(answer[i])