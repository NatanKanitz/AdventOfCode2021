import math

with open('input.txt') as f:
    lines = f.readlines()
    input = []
    for lineIndex, line in enumerate(lines):
        newLine = line.replace('\n', '')
        input.append(newLine)

def MostCommon(string):
    length = len(string)
    sum = 0
    for num in string:
        sum += int(num)

    if sum < math.ceil(length/2):
        return "0"
    else:
        return "1"

def LeastCommon(string):
    length = len(string)
    sum = 0
    for num in string:
        sum += int(num)
    if sum < math.ceil(length/2):
        return "1"
    else:
        return "0"

def binToDec(binary):
    length = len(binary)
    sum = 0
    for index, value in enumerate(binary):
        sum += 2**(length-1-index)*int(value)
    return sum

def PartOne():
    columns = []
    binGammaRate = ''
    binEpsilonRate = ''
    for lineIndex, line in enumerate(lines):
        newLine = line.replace('\n', '')
        for index, num in enumerate(newLine):
            if lineIndex == 0:
                columns.append(num)
            else:
                columns[index] += num

    for code in columns:
        binGammaRate += MostCommon(code)
        binEpsilonRate += LeastCommon(code)

    gammaRate = binToDec(binGammaRate)
    epsilonRate = binToDec(binEpsilonRate)

    print(f"gammaRate: {gammaRate}, epsilonRate: {epsilonRate}\nMultiplication: {gammaRate*epsilonRate}")

def FindRating(bitFinder):
    candidates = input
    i = 0
    while len(candidates) != 1:
        columns = [[x[y] for x in candidates] for y in range(len(candidates[0]))] # nested list comprehension
        bit = bitFinder(columns[i])
        candidates = [x for x in candidates if x[i] == bit]
        i += 1
    return candidates[0]

def PartTwo():
    BinOxygenRating = FindRating(MostCommon)
    OxygenRating = binToDec(BinOxygenRating)

    BinCO2Rating = FindRating(LeastCommon)
    CO2Rating = binToDec(BinCO2Rating)

    print(OxygenRating, CO2Rating, OxygenRating*CO2Rating)

PartTwo()
