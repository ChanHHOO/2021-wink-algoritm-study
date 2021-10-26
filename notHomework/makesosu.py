def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            
            for k in range(j+1, len(nums)):
                hap = nums[i] + nums[j] + nums[k]
                sw = 0
                for q in range(2, hap):
                    if hap % q == 0:
                        sw = 1
                        
                        break
                if sw == 0:
                    print(nums[i] , nums[j] , nums[k])
                    answer += 1

    return answer

solution([1,2,3,4]		)