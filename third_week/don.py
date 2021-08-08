def solution(price, money, count):
    answer = [i*price for i in range(1, count+1)]
    
    return sum(answer) - money if money - sum(answer) < 0 else 0