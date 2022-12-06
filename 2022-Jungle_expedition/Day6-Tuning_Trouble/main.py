#!/usr/bin/python3

import os, sys

def task1(input):

    lastChars = []
    index = 0

    while True:
        lastChars.insert(0, input[index])

        # print(index)
        # print(lastChars)
        # print(set(lastChars))

        if(index > 3):
            if len(lastChars) == len(set(lastChars)):
                return index
        
        index += 1
        
        if len(lastChars) > 4:
            lastChars.pop()
        

def task2(input):

    lastChars = []
    index = 0

    while True:
        lastChars.insert(0, input[index])

        # print(index)
        # print(lastChars)
        # print(set(lastChars))

        if(index > 13):
            if len(lastChars) == len(set(lastChars)):
                return index+1
        
        index += 1
        
        if len(lastChars) > 13:
            lastChars.pop()


def main():

    problem_name = sys.argv[1]
    with open(f"{problem_name}.txt") as f:
        input = f.readline()

    print(f"Task1: {task1(input)}")
    print(f"Task2: {task2(input)}")

    return 0

if __name__ == "__main__":
    main()
