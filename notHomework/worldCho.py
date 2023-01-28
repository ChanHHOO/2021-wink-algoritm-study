import sys

def getMinIdx(students, cases):
    minIdx = 0
    minVal = students[cases[0]][0]
    for i in range(1, len(cases)):
        # print(students[cases[i]][0], cases[i])
        if minVal > students[cases[i]][0]:
            minIdx = i
            minVal = students[cases[i]][0]
    return minIdx


input = sys.stdin.readline

n = int(input())

r = int(input())

recommends = list(map(int, input().split(" ")))

students = {i:[0, 0] for i in range(101)}
# recommend, isTop
cases = [0] * n

empty = n

for i in range(r):
    students[recommends[i]][0] += 1    
    if students[recommends[i]][1] == 0:
        if empty:
            cases[n-empty] = recommends[i]
            students[recommends[i]][1] = 1
            empty -= 1
        else:
            students[recommends[i]][1] = 1
            minIdx = getMinIdx(students, cases)
            students[cases[minIdx]] = [0, 0]

            for j in range(minIdx, n-1):
                cases[j] = cases[j+1]

            cases[-1] = recommends[i]
cases.sort()
for i in range(n):
    if cases[i] != 0:
        print(cases[i], end=" ")
print()