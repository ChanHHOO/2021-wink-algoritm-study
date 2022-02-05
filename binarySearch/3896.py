import sys
import math

t = int(sys.stdin.readline())

n = 1300000

primes =[]

a = [False, False] + [True] * (n-1)
    
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

for k in range(t):

    k = int(sys.stdin.readline())

    target = k

    while True:

        for i in range(2, int(math.sqrt(target)) + 1):

            if target % i == 0:

                break
        else:

            break

        target += 1

    if target == k:

        print(0)
        
        continue

    start = 0

    end = len(primes) - 1

    bigI = 0

    mid = 0
    
    while start <= end:

        mid = (start + end) // 2

        if primes[mid] == target:
            break
        elif primes[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    print(primes[mid] - primes[mid-1])            