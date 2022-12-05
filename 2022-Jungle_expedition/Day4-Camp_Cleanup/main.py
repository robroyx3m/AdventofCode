#!/usr/bin/python3

def task1(input):

    add = 0

    for line in input:
        elfsSections = line.split(',')

        firstElf = elfsSections[0].split('-')
        secondElf = elfsSections[1].split('-')

        firstElf = [int(x) for x in firstElf]
        secondElf = [int(x) for x in secondElf]

        # print(firstElf)
        # print(secondElf)

        if (firstElf[0] >= secondElf[0] and firstElf[1] <= secondElf[1]):
            add += 1
        elif (secondElf[0] >= firstElf[0] and secondElf[1] <= firstElf[1]):
            add += 1
    
    print(f'Task 1: {add}')
    

def task2(input):

    add = 0

    for line in input:
        elfsSections = line.split(',')

        firstElf = elfsSections[0].split('-')
        secondElf = elfsSections[1].split('-')

        firstElf = [int(x) for x in firstElf]
        secondElf = [int(x) for x in secondElf]

        firstElf = list(range(firstElf[0], firstElf[1]+1))
        secondElf = list(range(secondElf[0], secondElf[1]+1))

        # print(firstElf)
        # print(secondElf)

        for x in firstElf:
            if x in secondElf:
                add += 1
                break

    print(f'Task 2: {add}')


def main():
    
    # with open('testInput.txt') as i:
    #     input = [line.rstrip() for line in i]
    
    with open('sectionAssignments.txt') as i:
        input = [line.rstrip() for line in i]

    task1(input)
    task2(input)


if __name__ == '__main__':
    main()