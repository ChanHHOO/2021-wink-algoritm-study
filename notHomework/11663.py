import sys
import copy

# n은 nums를 셋 한 길이
def findNum(num, cnt, used):
    #aa
    if cnt == m:
        try:
            answer[num] += 1
        except:
            answer[num] = 0
            print(num)
    else:
        for j in range(0, n):
            if used[j] == 0:
                new_used = copy.deepcopy(used)
                new_used[j] = 1
                findNum(num + " " + nums[j], cnt + 1, new_used)

input = sys.stdin.readline

n, m = map(int, input().split(" "))

nums = list(map(int, input().split(" ")))

nums.sort()

for i in range(n):
    nums[i] = str(nums[i])

answer = dict()

for i in range(n):
    used = [0] * n
    used[i] = 1
    findNum(nums[i], 1, used)
