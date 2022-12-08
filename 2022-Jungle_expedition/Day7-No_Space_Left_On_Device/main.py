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

    directories = []
    innerDirSize = []
    upperDirSize = []

    index = 0

    for line in input:
        # print(line)  
        if 'cd ' in line:
            # print(line.split(" "))
            directories.append(line.split()[2])
            innerDirSize.append(0)
            upperDirSize.append(0)
            curIndex = index
            index += 1  
        if re.search("[0-9].*", line):
            innerDirSize[curIndex] += int(line.split(" ")[0])
    
    for i in directories:
        if not (i == '/' or i == '..'):
            curIndex = directories.index(i)
            tmp = curIndex+1
            while tmp < len(directories):
                if directories[tmp] == '..':
                    break
                tmp += 1
            upperDirSize[curIndex] = sum(innerDirSize[curIndex:tmp])

    totalSize = 0
    for a in upperDirSize:
        if a <= 100000: 
            totalSize += a
    
    print(directories)
    print(innerDirSize)
    print(upperDirSize)
    
    return totalSize


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
