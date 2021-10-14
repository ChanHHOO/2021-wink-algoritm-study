answers = []
while True:
    n, m = map(int, input().split(" "))
    if n ==0 and m == 0:
        break
    land = []
    allow = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    landTree = {}
    for i in range(m):
        tmp = list(map(int, input().split(" ")))
        tmp.append(0)
        land.append(tmp)
    land.append([0 for _ in range(n+1)])
        

    for i in range(m):
        for j in range(n):
            if land[i][j] == 1:
                if (i, j) not in landTree.keys():
                    landTree[(i, j)] = []
                for k in range(8):
                    if land[i + allow[k][0]][j + allow[k][1]] == 1:
                        landTree[(i, j)].append((i+allow[k][0], j+allow[k][1]))

    visit = []
    queue = []
    
    answer = 0
    while list(landTree.keys()) != []:
        queue.append(list(landTree.keys())[0])
        while queue:
            node = queue.pop(0)
            if node not in visit:
                visit.append(node)
                
                queue.extend(landTree[node])

                landTree.pop(node)
        answer += 1
    answers.append(answer)
for i in answers:
    print(i)