import sys

n = int(sys.stdin.readline())

nums = [0]

for _ in range(n):

    nums.append(int(sys.stdin.readline()))


def dfs(ci):

    numList = []

    visit = [False for _ in range(n+1)]

    nextNode = ci

    while True:

        currentNode = nextNode

        if visit[currentNode] == False:

            nextNode = nums[currentNode]

            numList.append(currentNode)

            visit[currentNode] = True

        if nextNode == ci:

            break

        if visit[nextNode] == True:

            numList = []

            break
            
    return numList


answer = []

for i in range(1, n+1):

    if i == nums[i]:
        answer.append(i)
    else:
        answer += dfs(i)

answer = sorted(list(set(answer)))

print(len(answer))

for i in range(len(answer)):
    print(answer[i])








