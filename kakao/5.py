
def solution(box):
    # Write your code here
    while True:
        maxVal = max(box)
        maxIdx = box.index(maxVal)
        if maxIdx != 0:
            minVal = min(box[:maxIdx])
            minIdx = box.index(minVal)
        else:
            break

        if maxVal - minVal <= 1:
            break
        box[minIdx] += 1
        box[maxIdx] -= 1
    return max(box)
s