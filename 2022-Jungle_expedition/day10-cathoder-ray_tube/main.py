#!/usr/bin/python3

""" Day10 AoC
    https://adventofcode.com/2022/day/10
"""

import sys

def task1(data):
    """ Task 1 solution """
    x_reg = 1
    cycle = 1
    read_new_line = True
    next_line = 0
    next_add = 1
    output = []

    # print(data)

    while cycle <= 220:
        if read_new_line:
            line = read_line(data=data, next_line=next_line)
            next_line += 1
            read_new_line = False
        if line[0] == 'noop':
            read_new_line = True

        if logging(cycle):
            # print(x_reg, cycle, x_reg*cycle)
            output.append(x_reg*cycle)

        # print(f'cycle: {cycle}, x = {x_reg}')
        cycle += 1


        if line[0] == 'addx':
            if not next_add:
                x_reg += int(line[1])
                next_add = 1
                read_new_line = True
            else:
                next_add -= 1

    return sum(output)


def task2(data):
    """ Task 2 solution """

    x_reg = 1
    pixels = []
    sprite = [x_reg-1, x_reg, x_reg+1]

    cycle = 1
    read_new_line = True
    next_line = 0
    next_add = 1

    while cycle <= 240:
        if read_new_line:
            line = read_line(data=data, next_line=next_line)
            next_line += 1
            read_new_line = False

        if line[0] == 'noop':
            read_new_line = True

        pixels.append(pixel_value(sprite=sprite, pixel_index=cycle-1))

        # print(f'cycle: {cycle}, x = {x_reg}')
        # print(sprite)
        cycle += 1

        if line[0] == 'addx':
            if not next_add:
                x_reg += int(line[1])
                next_add = 1
                read_new_line = True
            else:
                next_add -= 1

        sprite = [x_reg-1, x_reg, x_reg+1]

    draw(data=pixels)
    return 0


def pixel_value(sprite, pixel_index):
    """ Check if pixel shall be lit or dark and return the value. """

    pixel = {
        'lit':'#',
        'dark':'.'
    }

    # print(sprite, pixel_index+1, pixel_index, pixel_index%40)
    ret = pixel['lit'] if pixel_index%40 in sprite else pixel['dark']

    return ret


def read_line(data, next_line):
    """ Read next line of instruction and return it with cmd and argument separated"""
    try:
        line = data[next_line]
    except IndexError:
        print('Finished input file')
        sys.exit(1)

    # print(f'line = {line}')
    line = line.split(" ")

    return line


def draw(data):
    """ Draw display output. """
    display = []

    for j in range(6):
        str_tmp = ''
        for i in range(40):
            str_tmp += data[40*j+i]
        display.append(str_tmp)

    print('\n'.join(display))


def logging(cycle):
    """ Checks if it's time to log data. """
    base = 20
    inc = 40
    log = False

    if any(cycle == base + inc*mult for mult in range(0,6)):
        log = True

    return log


def main():
    """ Imports data and executes task1 and task2 """

    problem_name = sys.argv[1]
    with open(f"{problem_name}", encoding="utf-8") as tmp:
        data = [line.rstrip() for line in tmp]

    print(f"Task1: {task1(data)}\n")
    print(f"Task2: {task2(data)}")

    return 0

if __name__ == "__main__":
    main()
