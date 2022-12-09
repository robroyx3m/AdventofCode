#!/usr/bin/python3

def task1(lowerSub, upperSub):
    
    totalPrioSum = 0

    with open('itemsinrucksacks.txt') as i:
        for line in i:
            lenString = len(list(line))-1
            halfString = int(lenString/2)

            comp_1 = list(line[:halfString])
            comp_2 = list(line[halfString:-1])

            match = [x for x in comp_1+comp_2 if x in comp_1 and x in comp_2]

            if match[0].islower():
                totalPrioSum += ord(match[0]) - lowerSub
            else:
                totalPrioSum += ord(match[0]) - upperSub

    print(f'Part 1: {totalPrioSum}')


def task2(lowerSub, upperSub):

    totalPrioSum = 0

    #with open('testinput.txt') as i:
    with open('itemsinrucksacks.txt') as i:
        rucksacks = [line.rstrip() for line in i]

        a = 0
        while True:
            match = [x for x in rucksacks[a]+rucksacks[a+1]+rucksacks[a+2] if x in rucksacks[a] and x in rucksacks[a+1] and x in rucksacks[a+2]]

            if match[0].islower():
                totalPrioSum += ord(match[0]) - lowerSub
            else:
                totalPrioSum += ord(match[0]) - upperSub
            
            a += 3
            if(a >= len(rucksacks)):
                break
    
    print(f'Part 2: {totalPrioSum}')
        
        


def main():

    '''
        1 = a => ord(a) - x = 1 => ord(a) - 1 = x
        27 = A => ord(A) - y = 27 => ord(A) - 27 = y
    '''

    lowerSub = ord('a') - 1
    upperSub = ord('A') - 27

    task1(lowerSub, upperSub)
    task2(lowerSub, upperSub)


if __name__ == '__main__':
    main()