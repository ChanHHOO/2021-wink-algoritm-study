import sys
from typing import AnyStr
def solution():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    l, r = sorted(nums[:len(nums)//2+1]), sorted(nums[len(nums)//2+1:])
    answer = 0
    for i in range(len(r)):

        for j in range(len(l)-1, -1, -1):
            print(r[i], l[j])
            if r[i] >= l[j]:
                break
            
            answer += 1
    print(answer)            

solution()