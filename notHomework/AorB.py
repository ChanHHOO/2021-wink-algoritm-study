a = input()
b = input()
i = 0
while True:
    if i > len(a) - 1:
        break
    if not a[i].isalpha():
        a = a[:i] + a[i+1:]
    i += 1
if b in a:
    print(1)
else:
    print(0)