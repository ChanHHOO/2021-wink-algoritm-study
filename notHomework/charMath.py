import sys

n = int(sys.stdin.readline())

alpha = {}
answer = 0
alphabet_list = []

for i in range(65, 91):alpha[chr(i)] = 0

words = []

for _ in range(n):
    a = sys.stdin.readline()
    words.append(a[:-1])
for alphabet in words:
    for i in range(len(alphabet)):
        num = 10 ** (len(alphabet) - i - 1)
        alpha[alphabet[i]] += num
for value in alpha.values():
    if value > 0:
        alphabet_list.append(value)

sorted_list = sorted(alphabet_list, reverse=True)

for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9 - i)
print(answer)

