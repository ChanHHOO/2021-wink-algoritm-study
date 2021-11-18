from collections import deque 
import sys
n, k = map(int, sys.stdin.readline().split(" "))
num = deque( sys.stdin.readline())
num.pop()

s = num.popleft()
cnt = 0
sw = 0
for i in range(len(num)):

    tmp = num.popleft()

    if s[-1] < tmp:
        
        while True:
            s = s[:-1]
            cnt += 1
            if cnt == k:
                sw = 1
                break
            if s == "" or s[-1] >= tmp:
                break
            
        s += tmp
    else:
        s += tmp
    if sw == 1:
        break

for i in range(len(num)):
    s += num.popleft()
if cnt != k:
    for i in range(k-cnt):
        s = s[:-1]
print(s)