with open('input.txt') as f:
    lines = f.readlines()
    input = []
    for lineIndex, line in enumerate(lines):
        newLine = line.replace('\n', '')
        input.append(newLine)
        inputArray = [int(x) for x in input[0].split(',')]

def FishProgression(fishes, days):
    for i in range(days):
        for index, fish in enumerate(fishes):
            if fish == 0:
                fishes[index] = 6
                fishes.append(9)
            else:
                fishes[index] -= 1
    return fishes

def PartOne():
    fishes = FishProgression(inputArray, 80)
    print(len(fishes))

def PartTwo():
    days = 256
    fishPerDay = [0]*9
    for fish in inputArray:
        fishPerDay[fish] += 1

    for i in range(days):
        dayZero = fishPerDay.pop(0)
        fishPerDay.append(dayZero)
        fishPerDay[6] += dayZero

    sum = 0
    for n in fishPerDay:
        sum += n

    print(sum)

PartTwo()
