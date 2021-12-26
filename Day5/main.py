from collections import defaultdict
import math

with open('input.txt') as f:
    lines = f.readlines()
    input = []
    for lineIndex, line in enumerate(lines):
        newLine = line.replace('\n', '')
        input.append(newLine)

def getPoints(x1, y1, x2, y2):
    points = set()
    if (x1 != x2) and (y1 != y2):
        deltaX = abs(x2-x1)
        deltaY = abs(y2-y1)
        if deltaX == deltaY: # Part Two
            stepX = deltaX//(x2-x1)
            stepY = deltaY//(y2-y1)
            for i in range(deltaX):
                points.add((x1+i*stepX, y1+i*stepY))
            points.add((x2,y2))
        return points
    if (x1 == x2) and (y1 != y2):
        step = ((y2-y1)//abs(y2-y1))
        for yn in range(y1, y2, step):
            points.add((x2, yn))
    elif (y1 == y2) and (x1 != x2):
        step = ((x2-x1)//abs(x2-x1))
        for xn in range(x1, x2, step):
            points.add((xn, y2))
    points.add((x2,y2))
    return points

def Day5():
    d = defaultdict(int)
    for command in input:
        splitArray = command.split(" -> ")
        x1, y1 = [int(x) for x in splitArray[0].split(',')]
        x2, y2 = [int(x) for x in splitArray[1].split(',')]
        for point in getPoints(x1, y1, x2, y2):
            d[tuple(point)] += 1

    print(len([d[point] for point in d if d[point] >= 2]))

Day5()
