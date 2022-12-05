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
    


    

    


def main():
    
    # with open('testInput.txt') as i:
    #     sectionPairs = [line.rstrip() for line in i]
    
    with open('sectionAssignments.txt') as i:
        sectionPairs = [line.rstrip() for line in i]

    task1(sectionPairs)

if __name__ == '__main__':
    main()