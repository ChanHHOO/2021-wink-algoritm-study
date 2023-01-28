import sys


nums = list(map(int, input()))
hap = 0
if 0 in nums:
    for i in range(len(nums)):
        hap += nums[i]
    if hap % 3 == 0:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            print(nums[i], end="")
        print("")
    else:
        print(-1)
else:
    print(-1)

