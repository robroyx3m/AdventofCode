#!/usr/bin/python3


import sys

#
#     https://adventofcode.com/2022/day/9
# 


def task1(input):
    #           [x,y]
    coordHead = [0,0]
    coordTail = [0,0]
    tailVisits = []

    for line in input:
        if line[0] == 'R':
            for _ in range(0, int(line.split()[1])):
                coordHead[0] += 1

                if not touching(coordHead, coordTail) and coordHead[1] == coordTail[1]:
                    coordTail[0] += 1

                elif not touching(coordHead, coordTail):
                    coordTail[0] += 1
                    coordTail[1] += (coordHead[1] - coordTail[1])
                
                if coordTail not in tailVisits:
                    tailVisits.append(coordTail[:])
                # print(f'{line} coordHead {coordHead} coordTail {coordTail}')

        if line[0] == 'L':
            for _ in range(0, int(line.split()[1])):
                coordHead[0] -= 1

                if not touching(coordHead, coordTail) and coordHead[1] == coordTail[1]:
                    coordTail[0] -= 1

                elif not touching(coordHead, coordTail):
                    coordTail[0] -= 1
                    coordTail[1] += (coordHead[1] - coordTail[1])
                
                if coordTail not in tailVisits:
                    tailVisits.append(coordTail[:])
                # print(f'{line} coordHead {coordHead} coordTail {coordTail}')

        if line[0] == 'U':
            for _ in range(0, int(line.split()[1])):
                coordHead[1] += 1

                if not touching(coordHead, coordTail) and coordHead[0] == coordTail[0]:
                    coordTail[1] += 1

                elif not touching(coordHead, coordTail):
                    coordTail[1] += 1
                    coordTail[0] += (coordHead[0] - coordTail[0])
                
                if coordTail not in tailVisits:
                    tailVisits.append(coordTail[:])
                # print(f'{line} coordHead {coordHead} coordTail {coordTail}')

        if line[0] == 'D':
            for _ in range(0, int(line.split()[1])):
                coordHead[1] -= 1

                if not touching(coordHead, coordTail) and coordHead[0] == coordTail[0]:
                    coordTail[1] -= 1

                elif not touching(coordHead, coordTail):
                    coordTail[1] -= 1
                    coordTail[0] += (coordHead[0] - coordTail[0])
                
                if coordTail not in tailVisits:
                    tailVisits.append(coordTail[:])
                # print(f'{line} coordHead {coordHead} coordTail {coordTail}')
    
    return len(tailVisits)


def task2(input):
#   cord[0] = Head, cord[1] = tail_1 ... cord[9] = tail_9
#            [x,y]
    coord = [[0,0] for x in range(0,10)]
    tail9Visits = []

    for line in input:
        for _ in range(0, int(line.split()[1])):
            
            # print(mapped(coord))        
            
            if line[0] == 'R': 
                coord[0][0] += 1
                for pos in range(0,len(coord)-1):
                    coord = move(coord, pos, 0, 1, 1)  
                    if coord[9] not in tail9Visits:
                        tail9Visits.append(coord[9][:])   
            
            if line[0] == 'L': 
                coord[0][0] += -1
                for pos in range(0,len(coord)-1):
                    coord = move(coord, pos, 0, 1, -1)  
                    if coord[9] not in tail9Visits:
                        tail9Visits.append(coord[9][:])          
            
            if line[0] == 'U': 
                coord[0][1] += 1
                for pos in range(0,len(coord)-1):
                    coord = move(coord, pos, 1, 0, 1)  
                    if coord[9] not in tail9Visits:
                        tail9Visits.append(coord[9][:])   
            
            if line[0] == 'D': 
                coord[0][1] += -1
                for pos in range(0,len(coord)-1):
                    coord = move(coord, pos, 1, 0, -1)  
                    if coord[9] not in tail9Visits:
                        tail9Visits.append(coord[9][:])   
            
    print(f'{tail9Visits}')  
    return len(tail9Visits)


# def mapped(coord):
#     for index, pos in enumerate(coord):
#         tmp[pos[0]][pos[1]] = index
    
#     out = ''
#     return out.join(tmp)


def move(coord, pos, inc, nInc, value): # pos = current head/tail, inc = x or y (0 or 1), value is +1 or -1
    if not touching(coord[pos], coord[pos+1]) and coord[pos][nInc] == coord[pos+1][nInc]:
        coord[pos+1][inc] += value
    elif not touching(coord[pos], coord[pos+1]):
        coord[pos+1][inc] += value
        coord[pos+1][nInc] += (coord[pos][nInc] - coord[pos+1][nInc])
    return coord


def touching(posH, posT):
    if (abs(posH[0]-posT[0]) < 2 and abs(posH[1]-posT[1]) < 2):
        return True
    else:
        return False


def main():

    problem_name = sys.argv[1]
    with open(f"{problem_name}") as f:
        input = [line.rstrip() for line in f]

    print(f"Task1: {task1(input)}")
    print(f"Task2: {task2(input)}")

    return 0

if __name__ == "__main__":
    main()
