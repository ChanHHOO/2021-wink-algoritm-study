import sys
from collections import deque

answers = []

while True:
    
    tmp = list(sys.stdin.readline())
    s = deque(tmp[:-1])
    answer = 0

    if s[0] == '-':

        break
    
    t = s.popleft()

    if t == '}':
        answer += 1
    
    stack = ['{']

    for i in range(len(s)):

        c = s.popleft()

        if stack:

            if stack[-1] == '{' and c == '}':

                stack.pop()

            elif stack[-1] == '{' and c == '{':
            
                stack.append('{')

            
            

        else:
            stack.append('{')
            if c == '}':
                answer += 1
    if stack:
        answer += len(stack) // 2
    answers.append(answer)


for i in range(1, len(answers) + 1):
    print(str(i) + ". " + str(answers[i-1]))

    
        


