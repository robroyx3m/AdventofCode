#!/usr/bin/python3

def main():
    food = []
    totalCaloriesPerElf = []

    with open('calorycountPerElf.txt') as i:
        for line in i:
            if line == '\n':
                totalCaloriesPerElf.append(sum(food))
                food.clear()
            elif not line:
                break
            else:
                food.append(int(line))

    sortedList = sorted(totalCaloriesPerElf, reverse=True)

    print(sortedList[0]+sortedList[1]+sortedList[2])

if __name__ == '__main__':
    main()