import sys

# 162, 81, 8, 4, 2, 1, 0

# 42, 21, 2, 1, 0

input = sys.stdin.readline

target, n = map(int, input().split(" "))
answer = 0
while(n):
    if target == n:
        break
    if n % 2 == 0:
        n //= 2
    elif(n >= 10):
        tmp = str(n)
        if tmp[-1] != '1':
            answer = -2
            break
        n = int(tmp[:-1])
    else:
        answer = -2
        break        
    answer += 1
    
else:
    answer = -2
print(answer+1)