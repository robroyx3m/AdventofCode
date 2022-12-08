#!/usr/bin/python3


import sys

#
#     https://adventofcode.com/2022/day/8
# 


def task1(input):
    # First add all trees on edges
    visTreesSum = 0

    # visTreeCords = [(x0,y0), (x1,y1)]

    # Top line
    visTreesCoord = [(x,0) for x in range(len(input[0]))]
    # Left line
    visTreesCoord += [(0,x) for x in range(1, len(input))]
    # Bottom line
    visTreesCoord += [(x,(len(input)-1)) for x in range(1, len(input))]
    # Right line
    visTreesCoord += [(len(input[0])-1,x) for x in range(1, len(input)-1)]

    # print(visTreesCoord)

    y = 1
    while y < len(input)-1:
        x = 1
        while x < len(input[0])-1:
            tree = input[y][x]

            # Check left:
            if all((input[y][tmp] < tree) for tmp in range(0, x)):
                visTreesCoord.append((x, y))
                # print((x,y))
                
            # Check right:
            if all((input[y][tmp] < tree) for tmp in range(x+1, len(input[0]))):
                if not (x,y) in visTreesCoord:
                    visTreesCoord.append((x, y))
                    # print((x,y))
            
            # Check up:
            if all((input[tmp][x] < tree) for tmp in range(0, y)):
                if not (x,y) in visTreesCoord:
                    visTreesCoord.append((x, y))
                    # print((x,y))

            # Check down:
            if all((input[tmp][x] < tree) for tmp in range(y+1, len(input))):
                if not (x,y) in visTreesCoord:
                    visTreesCoord.append((x, y))
                    # print((x,y))

            x += 1
        y += 1

    # print(f'\n{visTreesCoord}\n')

    return len(set(visTreesCoord))


def task2(input):
    
    y = x = 1    
    scenicScore = 1

    y = 1
    while y < len(input)-1:
        x = 1
        while x < len(input[0])-1:
            tree = input[y][x]
            curScore = [0, 0, 0, 0]
            
            # Check left
            for tmp in range(x-1, -1, -1):
                if input[y][tmp] < tree:
                    curScore[0] += 1
                else:
                    curScore[0] += 1
                    break
            # Check right
            for tmp in range(x+1, len(input[0])):
                if input[y][tmp] < tree:
                    curScore[1] += 1
                else:
                    curScore[1] += 1
                    break
            # Check up
            for tmp in range(y-1, -1, -1):
                if input[tmp][x] < tree:
                    curScore[2] += 1
                else:
                    curScore[2] += 1
                    break
            # Check down
            for tmp in range(y+1, len(input)):
                if input[tmp][x] < tree:
                    curScore[3] += 1
                else:
                    curScore[3] += 1
                    break
            x += 1
            tmp = curScore[0]*curScore[1]*curScore[2]*curScore[3]
            if tmp > scenicScore:
                scenicScore = tmp 
        y += 1
    
    return scenicScore


def main():

    problem_name = sys.argv[1]
    with open(f"{problem_name}") as f:
        input = [line.rstrip() for line in f]

    print(f"Task1: {task1(input)}")
    print(f"Task2: {task2(input)}")

    return 0

if __name__ == "__main__":
    main()
