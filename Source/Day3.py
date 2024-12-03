from AoCUtilities import *
import re



def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sumMuls = 0
    for fileLine in fileData:
        possibleValidOptions = fileLine.split('mul(')

        for option in possibleValidOptions:
            index = option.find(',')
            if index == -1:
                continue
            firstNumStr = option[0:index]
            if not firstNumStr.isnumeric() or ' ' in firstNumStr:
                continue
            firstNum = int(firstNumStr)
            parenIndex = option.find(')', index+1)
            if parenIndex == -1:
                continue
            secondNumStr = option[index+1:parenIndex]
            if not secondNumStr.isnumeric() or ' ' in secondNumStr:
                continue
            secondNum = int(secondNumStr)
            sumMuls += firstNum * secondNum

    return sumMuls

def FindClosestIndex(val, indexList: list) -> int:
    closest = -1
    for index in indexList:
        if index < val:
            closest = index
    return closest


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.read()

    sumMuls = 0
    fileLine = fileData
    possibleValidOptions = re.finditer('mul\(\d+,\d+\)', fileLine)
    dos = re.finditer('do\(\)', fileLine)
    donts = re.finditer('don\'t\(\)', fileLine)

    dosIndices = [x.start() for x in dos]
    dontsIndices = [x.start() for x in donts]
    for optionIter in possibleValidOptions:
        mulStartIndex = optionIter.start()
        dosClosest = FindClosestIndex(mulStartIndex, dosIndices)
        dontsClosest = FindClosestIndex(mulStartIndex, dontsIndices)

        if dontsClosest > dosClosest:
            continue

        option = optionIter.group()
        nums = re.findall('\d+',option)
        firstNum = int(nums[0])
        secondNum = int(nums[1])
        sumMuls += firstNum * secondNum


    return sumMuls

filePath = "C:\\dev\\AdventOfCode2024\\Input\\Day3.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))