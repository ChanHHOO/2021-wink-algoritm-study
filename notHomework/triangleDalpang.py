def solution(n):
    answer = []
    triangle = [[0]*i for i in range(1, n+1)]
    cnt = 1
    l, b, r = 0, n-1, n-2
    nc = 0
    while n >= 0:

        for i in range(n):
            triangle[nc + i][l] = cnt
            cnt += 1

        l += 1
        n -= 1
        for i in range(n):
            triangle[b][l+i] = cnt
            cnt += 1
        b -= 1
        n -= 1


        rc = r
        for i in range(n):
            triangle[b-i][rc] = cnt
            cnt += 1
            rc -= 1
        r -= 2
        n -= 1

        nc += 2

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            answer.append(triangle[i][j])
    return answer

print(solution(6))