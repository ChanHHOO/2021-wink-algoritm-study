def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

n = int(input())
nList = list(map(int, input().split(" ")))
nList = merge_sort(nList)
m = int(input())
mList = list(map(int, input().split(" ")))

answer = []
for card in mList:
    target = (len(nList) // 2)-1
    sw = 0
    start = 0
    end = len(nList) - 1
    while start <= end:
        mid = (start + end) // 2
        if nList[mid] == card:
            answer.append('1')
            sw = 1
            break
        if nList[mid] < card:
            start = mid + 1
        else:
            end = mid - 1
    if sw == 0:
        answer.append('0')
            


        
        
        
print(" ".join(answer))