import sys

# n은 nums를 셋 한 길이
def findNum(m, n, nums, i, num, cnt):
    # print(i, num)
    # a = input()
    if cnt == m:
        try:
            answer[num] += 1
        except:
            print(num)
            answer[num] = 0
        return

    for j in range(i, n):
        findNum(m, n, nums, j, num +" "+ nums[j], cnt + 1)



input = sys.stdin.readline

n, m = map(int, input().split(" "))

nums = input().split(" ")

nums = list(set(nums))

for i in range(len(nums)):
    nums[i] = int(nums[i])

nums.sort()

for i in range(len(nums)):
    nums[i] = str(nums[i])

nLength = len(nums)

answer = dict()

for i in range(nLength):
    findNum(m, nLength, nums, i, nums[i], 1)
