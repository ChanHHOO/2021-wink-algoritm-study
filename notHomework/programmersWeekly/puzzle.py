import numpy as np

allow = [[1, 0], [0, 1], [-1, 0], [0, -1]]
blankList = []
puzzles = []
def bfs(gameBoard, boardVisit, ci, cj, size, isTable):
    nonB = 1 if isTable == True else 0

    q = [(ci, cj)]
    maxi = 0
    maxj = 0

    mini = 51
    minj = 51

    visitNode = []
    while q:
        
        node = q.pop(0)
        if boardVisit[node[0]][node[1]] == False:
            boardVisit[node[0]][node[1]] = True
            maxi = maxi if node[0] <= maxi else node[0]
            maxj = maxj if node[1] <= maxj else node[1]

            mini = mini if node[0] >= mini else node[0]
            minj = minj if node[1] >= minj else node[1]

            visitNode.append((node[0], node[1]))
            for i in range(4):
                if 0 <= node[0] + allow[i][0] < size and 0 <= node[1] + allow[i][1] < size:
                    if gameBoard[node[0] + allow[i][0]][node[1] + allow[i][1]] == nonB and boardVisit[node[0] + allow[i][0]][node[1] + allow[i][1]] == False:

                        q.append((node[0] + allow[i][0], node[1] + allow[i][1]))
    
    blank = [[0] * (maxj-minj+1) for _ in range((maxi-mini)+1)]
    for node in visitNode:
        blank[node[0] - mini][node[1] - minj] = 1

    tmp = 0
    sw = 0
    if isTable == True:
        for i in range(4):
            o = np.array(blank)
            blank = np.ndarray.tolist(np.rot90(o, 3))
            if blank in blankList:
                sw = 1
                blankList.remove(blank)
                for j in range(len(blank)):
                    for k in range(len(blank[j])):
                        if blank[j][k] == 1:
                            tmp += 1
            if sw == 1:
                return tmp
    else:
        blankList.append(blank)
    
    return tmp   
def solution(game_board, table):
    answer = 0
    size = len(game_board)
    boardVisit = [[False] * size for _ in range(size)]
    tableVisit = [[False] * size for _ in range(size)]



    for i in range(size):

        for j in range(size):
    
            if boardVisit[i][j] == False and game_board[i][j] != 1:

                bfs(game_board, boardVisit, i, j, size, False)


    for i in range(size):

        for j in range(size):
    
            if tableVisit[i][j] == False and table[i][j] != 0:

                answer += bfs(table, tableVisit, i, j, size, True)
        
            
            
    print(answer)

    return answer

solution(
    [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], 
    [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])