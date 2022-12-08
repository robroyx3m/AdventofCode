#!/usr/bin/python3


import os, sys, re
# from dataclasses import dataclass

#
#     https://adventofcode.com/2022/day/7
# 


def task1(input):

    '''

        What to do:
        build tree of folders
        sum size of individual folder
        sum total size of folder tree

    '''

    # cmd = {
    #     "cdTop" : 'cd /',
    #     "cdOut" : 'cd ..',
    #     "cdIn" : 'cd ',
    #     "list" : 'ls'
    # }

    directories = []
    dirSize = []

    index = 0

    for line in input:
        # print(line)  
        if 'cd ' in line:
            # print(line.split(" "))
            directories.append(line.split()[2])
            dirSize.append(0)
            curIndex = index
            index += 1  
        if re.search("[0-9].*", line):
            dirSize[curIndex] += int(line.split(" ")[0])

    print(directories)
    print(dirSize)

    return index



        

# def task2(input):




def main():

    problem_name = sys.argv[1]
    with open(f"{problem_name}.txt") as f:
        input = [line.rstrip() for line in f]

    print(f"Task1: {task1(input)}")
    # print(f"Task2: {task2(input)}")

    return 0

if __name__ == "__main__":
    main()
