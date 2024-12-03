from AoCUtilities import *

def IsRowSafe(rowData : list) -> bool:
    prevVal = -1
    isAscending = rowData[1] > rowData[0]
    for val in rowData:
        if prevVal == -1:
            prevVal = val
            continue
        if (val > prevVal) != isAscending:
            return False
        amountChanged = abs(val - prevVal)
        if amountChanged < 1 or amountChanged > 3:
            return False

        prevVal = val
    return True

def IsValSafe(val: int, prevVal: int, isAscending: bool) -> bool:
    if (val > prevVal) != isAscending:
        return False
    amountChanged = abs(val - prevVal)
    if amountChanged < 1 or amountChanged > 3:
        return False
    return True

def IsRowSafeB(rowData : list) -> bool:
    isAscending = True
    isAscending1 = rowData[1] > rowData[0]
    isAscending2 = rowData[2] > rowData[1]
    isAscending3 = rowData[3] > rowData[2]
    if isAscending1 == isAscending2:
        isAscending = isAscending1
    elif isAscending1 == isAscending3:
        isAscending = isAscending1
    else:
        isAscending = isAscending2


    rowDataCopy = rowData.copy()
    isSafe = True
    for index in range(1, len(rowData)):
        prevIndex = index-1
        if IsValSafe(rowData[index], rowData[prevIndex], isAscending):
            continue
        else:
            rowData.pop(index)
            isSafe = False
            break

    if isSafe:
        return True
    isSafe = True
    for index in range(1, len(rowData)):
        prevIndex = index-1
        if IsValSafe(rowData[index], rowData[prevIndex], isAscending):
            continue
        else:
            isSafe = False
            break

    if isSafe:
        return True
    isSafe = True
    for index in range(1, len(rowDataCopy)):
        prevIndex = index-1
        if IsValSafe(rowDataCopy[index], rowDataCopy[prevIndex], isAscending):
            continue
        else:
            rowDataCopy.pop(prevIndex)
            isSafe = False
            break
    if isSafe:
        return True

    isSafe = True
    for index in range(1, len(rowDataCopy)):
        prevIndex = index-1
        if IsValSafe(rowDataCopy[index], rowDataCopy[prevIndex], isAscending):
            continue
        else:
            isSafe = False
            break

    return isSafe

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    safeReports = 0
    for fileLine in fileData:
        dataLine = fileLine.strip().split(' ')

        rowData = [int(x) for x in dataLine]
        if IsRowSafe(rowData):
            safeReports += 1


    return safeReports

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    safeReports = 0
    for fileLine in fileData:
        dataLine = fileLine.strip().split(' ')

        rowData = [int(x) for x in dataLine]
        if IsRowSafeB(rowData):
            safeReports += 1


    return safeReports

filePath = "C:\\dev\\AdventOfCode2024\\Input\\Day2.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))