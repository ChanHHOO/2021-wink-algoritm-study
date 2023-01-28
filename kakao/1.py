
def solution(x, y, z):
    big = 0; small = 0
    
    if x > y:
        big = x; small = y
    else:
        big = y; small = x
    if z - (big - small) < 0: return -1
    else:
        print(((z - (big - small))//2) + y) 


if __name__ == '__main__':
    solution(2,4,9)