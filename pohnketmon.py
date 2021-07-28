def solution(nums):
    answer = len(set(nums))
    
    if answer > len(nums) // 2:
        answer = len(nums)//2
    return answer
solution([3, 1, 2, 3])