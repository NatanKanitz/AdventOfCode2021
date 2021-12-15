with open('input.txt') as f:
    lines = f.readlines()

def PartOne():
    xPos = 0
    depth = 0

    for line in lines:
        direction, amount = line.split(" ")
        amount = int(amount)

        if direction == "forward":
            xPos += amount
        elif direction == "up":
            depth -= amount
        else:
            depth += amount

    print(f"xPos: {xPos}, depth = {depth}\nMultiplication = {xPos*depth}")

def PartTwo():
    xPos = 0
    depth = 0
    aim = 0

    for line in lines:
        direction, amount = line.split(" ")
        amount = int(amount)

        if direction == "forward":
            xPos += amount
            depth += aim*amount
        elif direction == "up":
            aim -= amount
        else:
            aim += amount

    print(f"xPos: {xPos}, depth = {depth}\nMultiplication = {xPos*depth}")


PartTwo()
