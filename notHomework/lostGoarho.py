s = input()
tmp = ""
nums = []
for i in range(len(s)):
    if s[i].isdigit():
        tmp += s[i]
    else:
        if tmp:
            nums.append(int(tmp))
        tmp = s[i]
nums.append(int(tmp))
hap = 0
i = 0

while i != len(nums):
    if nums[i] < 0:
        hap += nums[i]
        i += 1
        while True:
            if i == len(nums) or nums[i] < 0:
                break
            hap += (nums[i]*-1)
            i += 1
    else:
        hap += nums[i]
        i += 1
print(hap)
