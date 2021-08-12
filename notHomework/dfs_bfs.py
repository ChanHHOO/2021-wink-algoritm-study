def solution():
    answer = []
    
    n, m, v = map(int, input().split(" "))
    node = []
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split(" "))
        node.append(a)
        node.append(b)
        graph[a-1].append(b)
        graph[b-1].append(a)
    length = len(set(node))
    
    
    #DFS
    for i in range(n):
        graph[i].sort(reverse=True)
    dfs = []
    stack = [v]
    while stack:
        node = stack.pop()
        if node not in dfs:
            dfs.append(node)
            stack.extend(graph[node-1])
    #BFS
    for i in range(n):
        graph[i].sort()
    bfs = []
    queue = [v]
    while queue:
        node = queue.pop(0)
        if node not in bfs:
            bfs.append(node)
            queue.extend(graph[node-1])
    #print
    dfsAnswer = ""
    bfsAnswer = ""
    for i in range(len(dfs)):
        dfsAnswer += str(dfs[i]) + " "
        bfsAnswer += str(bfs[i]) + " "
    print(dfsAnswer[:len(dfsAnswer)]+"\n"+bfsAnswer[:len(bfsAnswer)])
    return answer
solution()