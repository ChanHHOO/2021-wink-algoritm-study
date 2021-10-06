def solution(word):
    answer = 0
    alphas = ['A','E','I','O','U']
    correctWord = ""
    while correctWord != word:

        if len(correctWord) != 5:
            correctWord += "A"
            answer += 1
        else:
            if correctWord[-1] == 'U':
                while True:
                    if correctWord[-1] == 'U':
                        correctWord = correctWord[:-1]
                    else:
                        correctWord = correctWord[:-1] + alphas[alphas.index(correctWord[-1])+1]
                        break
            else:
                correctWord = correctWord[:-1] + alphas[alphas.index(correctWord[-1])+1]
            answer += 1
    print(answer)
    return answer

solution("UUUUU")