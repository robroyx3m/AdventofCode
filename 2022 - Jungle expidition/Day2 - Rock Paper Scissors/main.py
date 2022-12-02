#!/usr/bin/python3

'''!

    This turned out very ugly...

'''

def main():

    rock = 1
    paper = 2
    scissors = 3

    fail = 0
    draw = 3
    win = 6

    beat = {
        rock:scissors,
        paper:rock,
        scissors:paper
    }

    beat2 = {
        rock:paper,
        paper:scissors,
        scissors:rock
    }

    failList = {
        paper:rock,
        rock:scissors,
        scissors:paper
    }

    opponent = {
        'A':rock,
        'B':paper,
        'C':scissors
    }

    self = {
        'X':rock,
        'Y':paper,
        'Z':scissors
    }
    
    outcome = {
        'X':fail,
        'Y':draw,
        'Z':win
    }

    totalPoints_task1 = 0
    totalPoints_task2 = 0
    # totalLines = 0

    with open('encryptedStrategyGuide.txt') as i:
        for line in i:
            # totalLines += 1

            # print(f"Current line: {line}")

            oppMove = line[0]            
            selfMove = line[2]
            reqRes = line[2]

            totalPoints_task1 += self[selfMove]
            totalPoints_task1 += task1(opponent, oppMove, self, selfMove, fail, draw, win, beat)

            totalPoints_task2 += outcome[reqRes]
            totalPoints_task2 += task2(opponent, oppMove, outcome, reqRes, fail, draw, win, beat2, failList)
    
    # print(f"Total lines read: {totalLines}")
    print(f'Total points according to task 1: {totalPoints_task1}')
    print(f'Total points according to task 2: {totalPoints_task2}')


def task1(opponent, oppMove, self, selfMove, fail, draw, win, beat):
    pnts = 0
    # Draw
    if (opponent[oppMove] == self[selfMove]):
        pnts += draw
    
    # Win
    elif (beat[self[selfMove]] == opponent[oppMove]):
        pnts += win
    
    # Fail
    else:
        pnts += fail

    return pnts


def task2(opponent, oppMove, outcome, reqRes, fail, draw, win, beat, failList):
    pnts = 0

    match outcome[reqRes]:
        case 0:
            pnts = failList[opponent[oppMove]]
        case 3:
            pnts = opponent[oppMove]
        case 6:
            pnts = beat[opponent[oppMove]]

    return pnts


if __name__ == '__main__':
    main()