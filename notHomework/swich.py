import sys

n = int(input())

swich = list(map(int, sys.stdin.readline().split()))

studentNum = int(input())

students = []

for i in range(studentNum):
    students.append(list(map(int, sys.stdin.readline().split())))
# 남자 = 배수들 바꾸기, 여자 = 양 옆 같은 것들

for i in range(studentNum):

    if students[i][0] == 1:
        for j in range(students[i][1]-1, n, students[i][1]):
            swich[j] = 1 if swich[j] != 1 else 0
    else:
        j = 1
        swich[students[i][1]-1] = 1 if swich[students[i][1]-1] != 1 else 0
        while True:
            
            if students[i][1] - 1 - j >= 0 and students[i][1] - 1 + j < n:

                if swich[students[i][1] - 1 - j] == swich[students[i][1] - 1 + j]:
                    swich[students[i][1] - 1 - j] = 1 if swich[students[i][1] - 1 - j] != 1 else 0
                    swich[students[i][1] - 1 + j] = 1 if swich[students[i][1] - 1 + j] != 1 else 0
                else:
                    break
            else:
                break
            j += 1

swich = list(map(str, swich))

answer = " ".join(swich)
answer = answer[:41] + "\n" + answer[40:]

print(answer)
for i in range(2, n//20+1):
    answer = answer[:(40*i)+1] + "\n" + answer[40*i:]
print(answer)