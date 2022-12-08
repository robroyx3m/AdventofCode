#!/usr/bin/python3


import os, sys

#
#     https://adventofcode.com/2022/day/8
# 


def task1(input):
    # First add all trees on edges
    # visTreesSum = len(input[0])*2+(len(input)-2)*2
    # Top line
    visTreesCoord = [(x,0) for x in range(len(input[0]))]
    # Left line
    visTreesCoord += [(0,x) for x in range(1, len(input))]
    # Bottom line
    visTreesCoord += [(x,(len(input)-1)) for x in range(1, len(input))]
    # Right line
    visTreesCoord += [(len(input[0])-1,x) for x in range(1, len(input)-1)]

    # print(visTreesCoord)

    # for line in input:
    #     for entry in line:
    #         print(entry)
    
    index = 1
    while index < len(input)-2:
        subIndex = 1
        while subIndex < len(input[0])-2:
            # Check horizontal:
            for tree in input[index]:
                print(input[index])
                # print(input[index][subIndex])
                if tree < input[index][subIndex]:
                    visTreesCoord.append((subIndex, index))
                    break 
            subIndex += 1
        index += 1
    print(visTreesCoord)

    return visTreesSum



        

# def task2(input):




def main():

    problem_name = sys.argv[1]
    with open(f"{problem_name}") as f:
        input = [line.rstrip() for line in f]

    print(f"Task1: {task1(input)}")
    # print(f"Task2: {task2(input)}")

    return 0

if __name__ == "__main__":
    main()
