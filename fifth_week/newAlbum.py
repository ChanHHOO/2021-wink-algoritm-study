answer = 0
n = int(input()) #노래 갯수
l = int(input()) #노래 길이
c = int(input()) #cd 용량
tmp = 0
songs = 0
for i in range(n):
    tmp += l
    songs += 1
    if c-tmp < l+1:
        print(songs)
        if songs % 13 == 0:
            answer += 1
            tmp = l
        else:
            answer += 1
            tmp = 0
        songs = 0
        continue
    tmp += 1

if tmp != 0:
    answer += 1
print(answer)