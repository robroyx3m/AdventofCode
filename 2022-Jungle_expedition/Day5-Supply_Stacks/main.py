#!/usr/bin/python3

def task1(input):

    for line in input:
        if ' 1   2' in line:
            columns = int(line[-1])

    col = storeColumns(columns, input)

    for line in input:
        if 'move' in line:
            moves = line.split()
            amount = int(moves[1]) 
            f = int(moves[3]) # from
            to = int(moves[5])

            while amount > 0:
                col[to].append(col[f][-1])
                col[f].pop()

                amount -= 1

    word = ''
    del col[0]
    for x in col:
        word += x[-1]

    print(f'Task 1: {word}')


def task2(input):

    for line in input:
        if ' 1   2' in line:
            columns = int(line[-1])

    col = storeColumns(columns, input)

    for line in input:
        if 'move' in line:
            moves = line.split()
            amount = int(moves[1]) 
            f = int(moves[3]) # from
            to = int(moves[5])

            col[to] = col[to]+col[f][-amount:]
            col[f] = col[f][:-amount]

    word = ''
    del col[0]
    for x in col:
        word += x[-1]

    print(f'Task 2: {word}')
    

def storeColumns(columnsAmount, input):

    columns = [[] for i in range(columnsAmount+1)]

    for line in input:
        if ' 1   2' in line:
            break
        
        line = line[1:]

        a = 0
        while a <= columnsAmount:
            try:
                if(line[4*a] != ' '):
                    columns[a+1].insert(0, line[4*a])
            except:
                pass

            a += 1

    # print(columns)
 
    return columns  


def main():
    
    # with open('testInput.txt') as i:
    #     input = [line.rstrip() for line in i]
    
    with open('crates.txt') as i:
        input = [line.rstrip() for line in i]

    task1(input)
    task2(input)

if __name__ == '__main__':
    main()