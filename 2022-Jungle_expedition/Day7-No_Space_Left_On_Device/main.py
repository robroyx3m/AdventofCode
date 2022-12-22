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

    dirFiles = {}
    dirFolders = {}

    for line in input:
        # print(line)
        if '$ cd /' in line:
            dirFiles.update({'/':0})
            dirFolders.update({'/':''})
            curDir = '/'
        elif '$ cd ..' in line:
            pass
        elif 'dir ' in line:
            dirFolders[curDir] += f'{line.split(" ")[1]} '
        elif '$ cd ' in line:
            dirFiles.update({f'{line.split(" ")[2]}':0})
            dirFolders.update({f'{line.split(" ")[2]}':''})
            curDir = line.split(" ")[2]
        elif '$ ls' in line:
            pass
        elif re.search('[0-9]', line):
            dirFiles[curDir] += int(line.split(" ")[0])

    # print(dirFolders)
    # print()
    # print(dirFiles)
    # print()

    totalDirSizes = {}
    for key in dirFolders:
        # print(key)
        totalDirSizes.update({key:findFolderSizes(key, dirFiles, dirFolders)})

    goalDirs = 0
    for size in totalDirSizes.values():
        if size <= 100000:
            goalDirs += size

    print(totalDirSizes)
    print()

    return goalDirs


def findFolderSizes(posKey, files, folders):

    if folders[posKey] == '':
        # print(files[posKey])
        return files[posKey]   

    tmpSum = files[posKey]

    # print(folders[posKey].split(" "))

    for dir in folders[posKey].split(" "):
        if dir == '':
            break
        else:
            # print(dir)
            tmpSum += findFolderSizes(dir, files, folders)
    
    return tmpSum


# def task2(input):



# Run with ./main.py input.txt
def main():
    problem_name = sys.argv[1]
    with open(f"{problem_name}") as f:
        input = [line.rstrip() for line in f]

    print(f"Task1: {task1(input)}")
    # print(f"Task2: {task2(input)}")

    return 0

if __name__ == "__main__":
    main()
