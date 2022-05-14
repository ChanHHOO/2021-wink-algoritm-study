import sys

time = sys.stdin.readline().split()

for i in range(3):
    tmp  = tuple(time[i].split(":"))
    time[i] = tmp[0] + tmp[1]

chats = []
names = {}
answer = 0


while True:
    try:
        chats.append(sys.stdin.readline().split())
        names[chats[-1][1]] = 0
    except:
        break

if len(chats) > 1:
    for i in range(len(chats)):

        tmp = tuple(chats[i][0].split(":"))

        chatTime, name = (tmp[0] + tmp[1]), chats[i][1]

        if chatTime <= time[0]:
            names[name] += 1
        elif time[1] <= chatTime <= time[2] and names[name] == 1:
            names[name] += 1
            answer += 1
        
print(answer)