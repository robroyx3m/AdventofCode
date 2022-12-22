#!/usr/bin/python3

""" Day 13 AoC
    https://adventofcode.com/2022/day/13
"""

import sys


def task1(data):
    """ Task 1 solution """

    return 0


def task2(data):
    """ Task 2 solution """
    return 0




def main():
    """ Imports data and executes task1 and task2 """

    problem_name = sys.argv[1]
    with open(f"{problem_name}", encoding="utf-8") as tmp:
        data = [line.rstrip() for line in tmp]

    print(f"Task1: {task1(data)}\n")
    # print(f"Task2: {task2(data)}")

    return 0

if __name__ == "__main__":
    main()
