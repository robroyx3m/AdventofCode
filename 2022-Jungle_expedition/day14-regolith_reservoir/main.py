#!/usr/bin/python3


import sys, time

#
#     https://adventofcode.com/2022/day/14
# 


def task1(input):
    stonePos = findStoneCoord(input)
    sandPos = []

    rockBottom = max(a[1] for a in stonePos)

    drawMap(stonePos, sandPos)

    while True:
        curSandPos = [500,0]
        finished = False

        while True:
            firstTry = (curSandPos[0], curSandPos[1]+1)
            secTry = (curSandPos[0] - 1, curSandPos[1] + 1)
            thirdTry = (curSandPos[0] + 1, curSandPos[1] + 1)

            if curSandPos[1] == rockBottom:
                finished = True
                break
            if firstTry not in stonePos and firstTry not in sandPos:
                curSandPos[1] += 1
            elif secTry not in stonePos and secTry not in sandPos:
                curSandPos[0] -= 1
                curSandPos[1] += 1
            elif thirdTry not in stonePos and thirdTry not in sandPos:
                curSandPos[0] += 1
                curSandPos[1] += 1
            else:
                sandPos.append((curSandPos[0], curSandPos[1]))
                break

        if finished:
            break

    drawMap(stonePos, sandPos)

    return len(sandPos)


def task2(input):
    stonePos = findStoneCoord(input)
    sandPos = set()

    rockBottom = max(a[1] for a in stonePos) + 2

    stonePos.add((500,rockBottom))

    drawMap(stonePos, sandPos)

    start_time = time.time()

    while True:
        curSandPos = [500,0]

        while True:
            firstTry = (curSandPos[0], curSandPos[1]+1)
            secTry = (curSandPos[0] - 1, curSandPos[1] + 1)
            thirdTry = (curSandPos[0] + 1, curSandPos[1] + 1)

            if firstTry not in stonePos and firstTry not in sandPos and firstTry[1] != rockBottom:
                curSandPos[1] += 1
            elif secTry not in stonePos and secTry not in sandPos and secTry[1] != rockBottom:
                curSandPos[0] -= 1
                curSandPos[1] += 1
            elif thirdTry not in stonePos and thirdTry not in sandPos and thirdTry[1] != rockBottom:
                curSandPos[0] += 1
                curSandPos[1] += 1
            else:
                sandPos.add((curSandPos[0], curSandPos[1]))
                break

        if (500,0) in sandPos:
            break

    end_time = time.time()

    drawMap(stonePos, sandPos)

    print(f'Computation took: {end_time-start_time}s')

    return len(sandPos)


def drawMap(stonePos, sandPos):
    minX = 450
    maxX = 610
    minY = 0
    maxY = 163

    # for coord in stonePos:
    #     if coord[0] < minX:
    #         minX = coord[0]
    #     if coord[0] > maxX:
    #         maxX = coord[0]
    #     if coord[1] > maxY:
    #         maxY = coord[1]

    symbols = {
        'rock':'#',
        'air':'.',
        'sandOrigin':'+',
        'sandAtRest':'o'
    }

    map = []

    for j in range(maxY-minY+1):
        strTmp = ''
        for i in range(maxX-minX+1):
            if (minX+i,j) in stonePos:
                strTmp += symbols['rock']
            elif (minX+i,j) in sandPos:
                strTmp += symbols['sandAtRest']
            elif (minX+i,j) == (500,0):
                strTmp += symbols['sandOrigin']
            else:
                strTmp += symbols['air']
        map.append(strTmp)

    print(f'({minX},{minY}) ({maxX},{maxY})')
    print('\n'.join(map))


def findStoneCoord(input):
    tmp = []
    
    for i in input:
        line = i.split(' -> ')
        for index, xy in enumerate(line[:-1]):
            x0 = int(xy.split(',')[0])
            y0 = int(xy.split(',')[1])
            x1 = int(line[index+1].split(',')[0])
            y1 = int(line[index+1].split(',')[1])

            if x0 != x1:
                leftRight = int((x1-x0)/abs(x1-x0))
                tmp += ((xi, y0) for xi in range(x0,x1+leftRight,leftRight))
            else:
                upDown = int((y1-y0)/abs(y1-y0))
                tmp += ((x0, yi) for yi in range(y0,y1+upDown, upDown))

    return set(tmp) 


# Run with ./main.py input.txt
def main():
    problem_name = sys.argv[1]
    with open(f"{problem_name}") as f:
        input = [line.rstrip() for line in f]

    print(f"Task1: {task1(input)}")
    print(f"Task2: {task2(input)}")

    return 0

if __name__ == "__main__":
    main()
