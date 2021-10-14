def countNode(graph):

    visit = []
    visitIdx = 0
    for i in range(graph):
        node = graph.pop(0)
        for j in range(len(graph)):

            
        if node[0] >= visit[-1]:
            visitIdx += 1

        

def solution(n, wires):
    answer = -1
    for i in range(len(wires)):
        first = countNode(wires[:i] + wires[i+1:])

    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])