import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

answer = 0

def explore(i, j, answer):

    for ii in range(i, i + 2):
        for jj in range(j, j + 2):
            answer += 1
            if r == ii and jj == c:
                print(answer-1)
                exit

def zReq(n, i, j, ans):
    if n == 2:
        explore(i, j, ans)
    else:
        n //= 2
        if r < i + n and c < j + n:
            zReq(n, i, j, ans)

        if r >= i + n and c < j + n:
            zReq(n, i+n, j, ans + ((n*2)**2 // 2))

        if r < i + n and c >= j + n:
            zReq(n, i, j+n, ans + ((n*2)**2 // 4))
            
        if r >= i + n and c >= j + n:
            zReq(n, i + n, j + n, ans + ((n*2)**2 // 4) * 3)

        # n //= 2
        # zReq(n, r, c)
        # zReq(n, r, c + n)
        # zReq(n, r + n, c)
        # zReq(n, r + n, c + n)

zReq(2**n, 0, 0, 0)
