with open('input.txt') as f:
    lines = f.readlines()

def partOne():
    increased = 0
    numbers = []

    for index, line in enumerate(lines):
        number = int(line)
        numbers.append(number)

        if index and number > numbers[index - 1]:
            increased += 1

    print(increased)

def partTwo():
    groupSum = []
    increased = 0
    for index, line in enumerate(lines):
        number = int(line)

        if index == 0:
            groupSum.append(number)
        elif index == 1:
            groupSum.append(number)
            groupSum[index - 1] += number
        else:
            groupSum.append(number)
            groupSum[index - 1] += number
            groupSum[index - 2] += number

    for index, num in enumerate(groupSum):

        if index and num > groupSum[index - 1]:
            increased += 1

    print(increased)

partTwo()
