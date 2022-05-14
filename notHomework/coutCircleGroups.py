import sys

inDict = {}

outDict = {}
answer= 0
n = int(sys.stdin.readline())

for i in range(n):
    tmp = sys.stdin.readline()
    inDict[tmp[:-1]] = i+1
for i in range(n):
    tmp = sys.stdin.readline()
    outDict[tmp[:-1]] = i + 1

items = list(inDict.keys())

for i in range(n):
    if inDict[items[i]] > outDict[items[i]]:
        answer += 1
print(answer)
