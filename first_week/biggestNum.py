#옛날에 구글링 한 문제.
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))