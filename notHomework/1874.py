import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()
i = 0 

target = [int(input()) for _ in range(n)]
answer = []
for num in range(1, n+1):
  q.append(num)
  answer.append('+')
  while q and q[-1] == target[i]:
    q.pop()
    i += 1
    answer.append('-')



while q:
  num = q.pop()
  if target[i] == num:
    i += 1
    answer.append('-')

if i == len(target):
  for j in range(len(answer)):
    print(answer[j])
else:
  print('NO')