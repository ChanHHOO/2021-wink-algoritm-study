def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    final_list = ["" for _ in range(n)]
    
    for i in range(n):
        b = ""
        while(arr1[i] != 0):
            b += str(arr1[i] % 2)
            arr1[i] //= 2
        for j in range(n-len(b)):
            b += "0"
        arr1_bin.append(''.join(reversed(b)))
        
    for i in range(n):
        b = ""
        while(arr2[i] != 0):
            b += str(arr2[i] % 2)
            arr2[i] //= 2
        for j in range(n-len(b)):
            b += "0"
        arr2_bin.append(''.join(reversed(b)))
    
    for i in range(n):
        for j in range(n):
            if arr1_bin[i][j] == '1' or arr2_bin[i][j] == "1":
                final_list[i]+= "#"
            else:
                final_list[i] += " "
    
    return final_list

solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])