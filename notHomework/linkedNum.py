
n = int(input())

ja = len(str(n))

if ja == 1:
    print(n)
    exit()

nine = 9

answer = 0

for i in range(1, ja):

    answer += i * nine

    nine *= 10

a = int("9" * (ja-1))

n -= a

print(answer + (n * ja))