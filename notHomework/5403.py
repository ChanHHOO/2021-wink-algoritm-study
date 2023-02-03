import collections
import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    commands = list(input().rstrip())

    num_cnt = int(input())

    nums_tmp = input()
    nums_tmp = nums_tmp[1:-2]
    if num_cnt != 0:
        nums = deque(list(nums_tmp.split(',')))
    else:
        nums = deque()
    r_cnt = 0
    isError = False
    for command in commands:
        if command == "R":
            r_cnt += 1
        else:
            if len(nums) == 0:
                isError = True
                break
            if r_cnt % 2 == 0:
                nums.popleft()
            else:
                nums.pop()
    if r_cnt % 2 == 1:
        nums.reverse()
    if not isError:
        nums_list = list(nums)
        answer = ','.join(nums_list)
        print('['+answer+']')
    else:
        print("error")



