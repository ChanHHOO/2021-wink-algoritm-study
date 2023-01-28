import sys

def decrease(e, start, n):
    for i in range(start, n):
        e[i] -= 1

input = sys.stdin.readline

n = int(input().rstrip())

f = list(map(int, input().rstrip().split(" ")))

l = [0] * n

e = [i for i in range(n)]

for i in range(n):

    # if e[f[i]] == 0:
    #     l[f[i]] = i+1
    #     decrease(e, f[i], n)
    # else:
    for j in range(0, n):
        if e[j] == f[i]:
            l[j] = i + 1
            e[j] = -1
            decrease(e, j, n)
            break

for i in range(n):
    print(l[i], end=" ")
print()