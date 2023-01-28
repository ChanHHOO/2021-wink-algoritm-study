import sys

n, m = map(int, sys.stdin.readline().split(" "))

dic = {}

for i in range(n):
    dic[input()] = 0
answer = []
for i in range(m):
    name = input()
    try:
        dic[name] += 1
        answer.append(name)
    except:
        continue
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])