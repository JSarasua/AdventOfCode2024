from AoCUtilities import *

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sumTotal = 0

    firstList = []
    secondList = []

    for fileLine in fileData:
        rowData = fileLine.strip().split('   ')
        firstList.append(int(rowData[0]))
        secondList.append(int(rowData[1]))

    firstList.sort()
    secondList.sort()

    for index in range(0, len(firstList)):
        firstVal = firstList[index]
        secondVal = secondList[index]
        result = abs(firstVal - secondVal)
        sumTotal += result

    return sumTotal

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sumTotal = 0

    firstList = []
    secondList = []

    for fileLine in fileData:
        rowData = fileLine.strip().split('   ')
        firstList.append(int(rowData[0]))
        secondList.append(int(rowData[1]))

    for firstVal in firstList:
        count = secondList.count(firstVal)
        sumTotal += firstVal * count
    return sumTotal

filePath = "C:\\dev\\AdventOfCode2024\\Input\\Day1.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))