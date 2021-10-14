n = str(int(input()) + 1)
while True:
    s = 1
    if len(n)%2 == 0:s=0
    l = n[:len(n)//2]
    r = n[(len(n)//2)+s:]
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            isPal = 0
            break
    n = str(int(n)+1)
print(n)