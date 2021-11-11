def isBoom(x, y, px, py):
    x, y = x+px, y+py
    if -6 < x < 6 and -6 < y < 6:
        return True
    return False

def solution(dirs):
    answer = 0
    commands= list(dirs)
    cx, cy = 0, 0
    visitRoad = []
    for i in range(len(commands)):
        if commands[i] == "U" and isBoom(cx, cy, 0, 1):
            
            if [(cx, cy), (cx, cy+1)] not in visitRoad and [(cx, cy+1), (cx, cy)] not in visitRoad:
                visitRoad.append([(cx, cy), (cx, cy+1)])
            cy += 1
        elif commands[i] == "R" and isBoom(cx, cy, 1, 0):
            
            if [(cx, cy), (cx+1, cy)] not in visitRoad and [(cx+1, cy), (cx, cy)] not in visitRoad:
                visitRoad.append([(cx, cy), (cx+1, cy)])
            cx += 1
        elif commands[i] == "D" and isBoom(cx, cy, 0, -1):

            if [(cx, cy), (cx, cy-1)] not in visitRoad and [(cx, cy-1), (cx, cy)] not in visitRoad:
                visitRoad.append([(cx, cy), (cx, cy-1)])
            cy -= 1
        elif commands[i] == "L" and isBoom(cx, cy, -1, 0):

            if [(cx, cy), (cx-1, cy)] not in visitRoad and [(cx-1, cy), (cx, cy)] not in visitRoad:
                visitRoad.append([(cx, cy), (cx-1, cy)])
            cx -= 1
    return len(visitRoad)
solution("LULLLLLLU")