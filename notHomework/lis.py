def solution():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    sum = [1 for i in range(n)]
    low = [1 for i in range(n)]
    for i in range(len(nums)):

        for j in range(i):

            if nums[i] > nums[j]:

                sum[i] = max(sum[j]+1, sum[i])
        for j in range(len(nums)-1,len(nums)-1-i,-1):
            
            if nums[len(nums)-1-i] > nums[j]:

                low[len(nums)-1-i] = max(low[j]+1, low[len(nums)-1-i])
    for i in range(n):
        sum[i] += low[i]
    print(max(sum)-1)
solution()