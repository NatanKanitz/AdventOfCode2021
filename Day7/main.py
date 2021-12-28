import math

with open('input.txt') as f:
    lines = f.readlines()
    input = []
    for lineIndex, line in enumerate(lines):
        newLine = line.replace('\n', '')
        input.append(newLine)
        inputArray = [int(x) for x in input[0].split(',')]

def Median(nums):
    sum = 0
    for num in nums:
        sum += num
    return round(sum/len(nums))

def WeightedMedian(nums, median):
    sum = 0
    for num in nums:
        sum += num/(1 + abs(num-median))
    return round(sum/len(nums))

def ClosestPoint(nums, weightedMedian):
    min = 0
    for num in nums:
        min += num

    for i in range(weightedMedian-len(nums), weightedMedian+len(nums), 1):
        sum = 0
        for num in nums:
            sum += abs(num-i)
        if sum < min:
            min = sum

    return min

def PartOne():
    median = Median(inputArray)
    weightedMedian = WeightedMedian(inputArray, median)
    minPoint = ClosestPoint(inputArray, weightedMedian)

    print(minPoint)

def ClosestPointTwo(nums, median):
    min = 0
    for num in nums:
        min += num**2

    for i in range(median-len(nums), median+len(nums), 1):
        sum = 0
        for num in nums:
            diff = abs(num-i)
            sum += (1+diff)*diff/2
        # print(sum)
        if sum < min:
            min = sum

    return min

def PartTwo():
    median = Median(inputArray)
    minPoint = int(ClosestPointTwo(inputArray, median))

    print(minPoint)


PartTwo()
