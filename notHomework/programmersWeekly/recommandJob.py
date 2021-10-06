def solution(table, languages, preference):
    answer = ''
    tableList = [list(reversed(table[i].split(" "))) for i in range(5)]
    for i in range(5):
        for j in range(4):
            if tableList[j][-1] > tableList[j+1][-1]:
                tableList[j], tableList[j+1] = tableList[j+1], tableList[j]


    sums = []
    for i in range(5):
        p = 0
        for j in range(len(languages)):

            try:
                p += (tableList[i].index(languages[j])+1) * preference[j]

            except:
                continue
        sums.append(p)
    
    

    return tableList[sums.index(max(sums))][-1]


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))