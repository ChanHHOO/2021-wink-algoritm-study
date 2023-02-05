import sys

n, m = map(int, sys.stdin.readline().split())

tree_list = list(map(int, sys.stdin.readline().split()))

tree_dict = {}

for i in range(n):
    try:
        tree_dict[tree_list[i]] += 1
    except:
        tree_dict[tree_list[i]] = 1

trees = list(tree_dict.keys())
trees.sort(reverse=True)

bottom = 0
top = max(trees)
if sum(tree_list) == m:
    print(0)
    exit()
mid = (bottom + top) // 2
while bottom <= top:

    tmp = 0

    for i in range(len(trees)):
        if mid < trees[i]:
            tmp += (trees[i] - mid) * tree_dict[trees[i]]
    if tmp == m:
        break
    if tmp > m:
        for i in range(len(trees)-1, -1, -1):
            if mid >= trees[i]:
                trees.pop()
        bottom = mid + 1
    else:
        top = mid - 1
    mid = (bottom + top) // 2
print(mid)