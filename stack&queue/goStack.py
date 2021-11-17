command = ""
printNum = []

while True:

    programs = []

    n = []

    command = input()

    if command == "":
        continue
    if command == "QUIT":
        break

    while True:
        if command == "END" or command == "QUIT":
            break
        if command[0] == "N":
            n.append(int(command[4:]))
            programs.append(command[0:3])
        else:
            programs.append(command)
        command = input()
    cnt = int(input())
    
    for i in range(cnt):
        v = int(input())
        stack = [v]
        n_cp = n[::]
        for j in range(len(programs)):
            cmd = programs[j]
            tmp = "-"
            if cmd == "NUM":
                if len(stack) < 1:
                    stack.append("ERROR")
                    break
                tmp = n_cp.pop(0)
            elif cmd == "POP":
                if len(stack) < 1:
                    stack.append("ERROR")
                    break
                stack.pop()
            elif cmd == "INV":
                if len(stack) < 1:
                    stack.append("ERROR")
                    break
                tmp = stack.pop() * -1
            elif cmd == "DUP":
                if len(stack) < 1:
                    stack.append("ERROR")
                    break
                tmp = stack[-1]
            elif cmd == "SWP":
                if len(stack) < 2:
                    stack.append("ERROR")
                    break
                stack[-1], stack[-2] = stack[-2], stack[-1]
            elif cmd == "ADD":
                if len(stack) < 2:
                    stack.append("ERROR")
                    break
                tmp = stack.pop() + stack.pop()
            elif cmd == "SUB":
                if len(stack) < 2:
                    stack.append("ERROR")
                    break
                tmp = (stack.pop() - stack.pop()) * -1
            elif cmd == "MUL":
                if len(stack) < 2:
                    stack.append("ERROR")
                    break
                tmp = stack.pop() * stack.pop()
            elif cmd == "DIV":
                if len(stack) < 2:
                    stack.append("ERROR")
                    break
                a = stack.pop() 
                b = stack.pop()
                if a == 0:
                    stack.append("ERROR")
                    break
                a_um = 0 if a > 0 else 1
                b_um = 0 if b > 0 else 1
                bu = 1
                if a_um + b_um == 1:
                    bu = -1
                tmp = (b // a)*bu
            elif cmd == "MOD":
                if len(stack) < 2:
                    stack.append("ERROR")
                    break
                a = stack.pop() 
                b = stack.pop() 
                if a == 0:
                    stack.append("ERROR")
                    break
                b_um = 1 if b > 0 else -1
                tmp = (b % a)*b_um
            
            if tmp != "-" and abs(tmp) > 1000000000:
                stack.append("ERROR")
                break
            if tmp != "-":
                stack.append(tmp)

        if len(stack) == 1:
            printNum.append(stack.pop())
        else:
            printNum.append("ERROR")
    printNum.append("")
for i in printNum:
    print(i)
        
