import sys

t = int(sys.stdin.readline())
answers = []
for _ in range(t):

    n = int(sys.stdin.readline())

    members = []

    for _ in range(n):

        paperNum, meetingNum = map(int, sys.stdin.readline().split())
        
        members.append((paperNum, meetingNum))

    members.sort(key=lambda x : x[0])

    answer = 0

    min = members[0][1]

    for i in range(1, n):

        if members[i][1] > min:
            answer += 1
        else:
            min = members[i][1]
    answers.append(n - answer)

for i in answers:
    print(i)