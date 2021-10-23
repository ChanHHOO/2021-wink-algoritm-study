
def bfs(n, tree):
    
    visit = [False for i in range(n)]
    
    q = []

    q.extend(tree[0])

    while q:
        node = q.pop(0)
        if visit[node-1] == False:
            visit[node-1] = True



            for i in range(len(tree)):
                if node in tree[i]:
                    q.extend(tree[i])
    return abs(visit.count(True) - visit.count(False)) 

def solution(n, wires):
    answers = []

    for i in range(n-1):
        answers.append(bfs(n, wires[:i] + wires[i+1:]))
    print(answers)
    return min(answers)

solution(4, [[1,2],[2,3],[3,4]])