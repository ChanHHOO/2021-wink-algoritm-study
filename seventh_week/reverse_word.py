from typing import AnyStr


s_list = input()
ans = []

tmp = ""
g_sw = 0
for i in range(len(s_list)):

    if s_list[i] == ">":
        tmp += s_list[i]
        g_sw = 0
        ans.append(tmp)
        tmp = ""
    elif s_list[i] == "<" or g_sw == 1:
        if g_sw == 0:
            ans.append(tmp[::-1])
            tmp = ""
        tmp += s_list[i]
        g_sw = 1
    elif s_list[i] == " ":
        ans.append(tmp[::-1] + " ")
        tmp = ""
    else:
        tmp += s_list[i]
if tmp != "":ans.append(tmp[::-1])

answer = "".join(ans)

print(answer)

        
